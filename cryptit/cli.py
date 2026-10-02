import argparse
import os

from cryptit.ciphers.caesar import CaesarCipher
from cryptit.ciphers.vigenere import VigenereCipher
from cryptit.ciphers.affine import AffineCipher
from cryptit.ciphers.hill import HillCipher
from cryptit.ciphers.playfair import PlayfairCipher
from cryptit.ciphers.rsa import RSACipher

RSA_KEYS_FILE = "cryptit_rsa_keys.txt"

def correct_path(string):
    if not string.lower().endswith(".txt"):
        raise argparse.ArgumentTypeError(
            "file must have a .txt extension"
        )
    if not os.path.isfile(string):
        raise argparse.ArgumentTypeError(
            "file does not exist"
        )
    return string

def positive_int(value):
    try:
        value = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            "iterations must be an integer"
        )
    if value < 1:
        raise argparse.ArgumentTypeError(
            "iterations must be greater than 0"
        )
    return value

def create_parser():
    parser = argparse.ArgumentParser(
        prog="cryptit",
        description="CryptIt - educational cryptography toolkit"
    )

    parser.add_argument(
        "--cipher",
        required=True,
        choices=[
            "caesar",
            "vigenere",
            "affine",
            "hill",
            "playfair",
            "rsa"
        ],
        help="Cipher to use"
    )

    parser.add_argument(
        "--key",
        type=str,
        help="Encryption/decryption key"
    )

    parser.add_argument(
        "--generate-keys",
        action="store_true",
        help="Generate RSA key pair"
    )

    parser.add_argument(
        "--iterations",
        type=positive_int,
        default=1,
        help="Number of cipher iterations (default: 1), doesnt work with rsa"
    )

    input_group = parser.add_mutually_exclusive_group(
        required=False
    )

    input_group.add_argument(
        "--text",
        type=str,
        help="Text to encrypt or decrypt"
    )

    input_group.add_argument(
        "--file",
        type=correct_path,
        help="Input file"
    )

    parser.add_argument(
        "--decrypt",
        action="store_true",
        help="Decrypt instead of encrypt"
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    return parser


def parse_rsa_key(key):
    if not key:
        return None

    parts = key.split(",")

    if len(parts) != 3:
        raise ValueError(
            "RSA key must have format e,d,n"
        )

    try:
        e, d, n = map(int, parts)
    except ValueError:
        raise ValueError(
            "RSA key values must be integers"
        )

    if e <= 0 or d <= 0 or n <= 0:
        raise ValueError(
            "RSA key values must be greater than 0"
        )

    return e, d, n


def save_rsa_keys(e, d, n):
    with open(RSA_KEYS_FILE, "w", encoding="utf-8") as file:
        file.write("CryptIt RSA Keys\n")
        file.write("================\n\n")

        file.write("Public key:\n")
        file.write(f"e = {e}\n")
        file.write(f"n = {n}\n\n")

        file.write("Private key:\n")
        file.write(f"d = {d}\n")
        file.write(f"n = {n}\n\n")

        file.write("Full key format for CryptIt:\n")
        file.write(f"{e},{d},{n}\n")


def validate_args(parser, args):
    if args.generate_keys:
        if args.cipher != "rsa":
            parser.error(
                "--generate-keys can only be used with --cipher rsa"
            )
        if args.key is not None:
            parser.error(
                "--generate-keys cannot be used together with --key"
            )
        if args.text is not None or args.file is not None:
            parser.error(
                "--generate-keys cannot be used with --text or --file"
            )
        if args.decrypt:
            parser.error(
                "--generate-keys cannot be used with --decrypt"
            )
        return
    if args.text is None and args.file is None:
        parser.error(
            "one of --text or --file is required"
        )
    if args.cipher == "rsa":
        if args.iterations != 1:
            parser.error(
                "RSA does not support iterations"
            )
        if args.key is not None:
            try:
                parse_rsa_key(args.key)
            except ValueError as error:
                parser.error(str(error))
        return

    if args.key is None:
        match args.cipher:
            case "caesar":
                parser.error(
                    "--cipher caesar requires --key"
                )

            case "vigenere":
                parser.error(
                    "--cipher vigenere requires --key"
                )

            case "affine":
                parser.error(
                    "--cipher affine requires --key in format a,b"
                )

            case "hill":
                parser.error(
                    "--cipher hill requires --key "
                    "in matrix format e.g. x,x;x,x"
                )

            case "playfair":
                parser.error(
                    "--cipher playfair requires --key"
                )


def read_input(args):
    if args.text is not None:
        return args.text
    with open(args.file, "r", encoding="utf-8") as file:
        return file.read()


def process_rsa(args, text):
    if args.key is None:
        e, d, n = RSACipher.generate_keys()

        save_rsa_keys(e, d, n)

        print("RSA key pair generated.")
        print(f"Keys saved to: {RSA_KEYS_FILE}")
        print()
        print("Public key:")
        print(f"e = {e}")
        print(f"n = {n}")
        print()
        print("Private key:")
        print(f"d = {d}")
        print(f"n = {n}")
        print()

    else:
        e, d, n = parse_rsa_key(args.key)

    if args.decrypt:
        encrypted_values = []

        for value in text.strip().split(","):
            try:
                encrypted_values.append(int(value))
            except ValueError:
                raise ValueError(
                    "RSA ciphertext must contain integers "
                    "separated by commas"
                )

        return RSACipher.decrypt(
            encrypted_values,
            d,
            n
        )

    encrypted = RSACipher.encrypt(
        text,
        e,
        n
    )

    return ",".join(map(str, encrypted))


def process_cipher(args, text):
    if args.cipher == "rsa":
        return process_rsa(args, text)

    result = text

    for _ in range(args.iterations):
        match args.cipher:

            case "caesar":
                key = int(args.key)

                if args.decrypt:
                    result = CaesarCipher.decrypt(
                        result,
                        key
                    )
                else:
                    result = CaesarCipher.encrypt(
                        result,
                        key
                    )

            case "vigenere":
                if args.decrypt:
                    result = VigenereCipher.decrypt(
                        result,
                        args.key
                    )
                else:
                    result = VigenereCipher.encrypt(
                        result,
                        args.key
                    )

            case "affine":
                a, b = map(int, args.key.split(","))

                if args.decrypt:
                    result = AffineCipher.decrypt(
                        result,
                        a,
                        b
                    )
                else:
                    result = AffineCipher.encrypt(
                        result,
                        a,
                        b
                    )

            case "hill":
                if args.decrypt:
                    result = HillCipher.decrypt(
                        result,
                        args.key
                    )
                else:
                    result = HillCipher.encrypt(
                        result,
                        args.key
                    )

            case "playfair":
                if args.decrypt:
                    result = PlayfairCipher.decrypt(
                        result,
                        args.key
                    )
                else:
                    result = PlayfairCipher.encrypt(
                        result,
                        args.key
                    )

            case _:
                raise ValueError(
                    f"Unknown cipher: {args.cipher}"
                )

    return result


def main():
    parser = create_parser()
    args = parser.parse_args()

    validate_args(parser, args)

    if args.generate_keys:
        e, d, n = RSACipher.generate_keys()

        save_rsa_keys(e, d, n)

        print("RSA key pair generated.")
        print(f"Keys saved to: {RSA_KEYS_FILE}")
        return

    text = read_input(args)
    result = process_cipher(args, text)

    if args.verbose:
        print(f"Cipher: {args.cipher}")
        print(f"Key: {args.key}")
        print(f"Iterations: {args.iterations}")
        print(f"Decrypt: {args.decrypt}")
        print()

    print(result)


if __name__ == "__main__":
    main()