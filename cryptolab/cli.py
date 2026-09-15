import argparse
import os

from cryptolab.ciphers.caesar import CaesarCipher

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
    value = int(value)

    if value < 1:
        raise argparse.ArgumentTypeError(
            "iterations must be greater than 0"
        )

    return value


def create_parser():
    parser = argparse.ArgumentParser(
        prog="cryptolab",
        description="CryptoLab - educational cryptography toolkit"
    )

    parser.add_argument(
        "--cipher",
        required=True,
        choices=["caesar"],
        help="Cipher to use"
    )

    parser.add_argument(
        "--key",
        type=int,
        help="Encryption/decryption key"
    )

    parser.add_argument(
        "--iterations",
        type=positive_int,
        default=1,
        help="Number of cipher iterations (default: 1)"
    )

    input_group = parser.add_mutually_exclusive_group(required=True)

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


def validate_args(parser, args):
    if args.cipher == "caesar" and args.key is None:
        parser.error(
            "--cipher caesar requires --key"
        )

def read_input(args):
    if args.text is not None:
        return args.text

    with open(args.file, "r", encoding="utf-8") as file:
        return file.read()

def process_cipher(args, text):
    if args.cipher == "caesar":
        result = text

        for _ in range(args.iterations):
            if args.decrypt:
                result = CaesarCipher.decrypt(result, args.key)
            else:
                result = CaesarCipher.encrypt(result, args.key)

        return result


def main():
    parser = create_parser()
    args = parser.parse_args()

    validate_args(parser, args)

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
