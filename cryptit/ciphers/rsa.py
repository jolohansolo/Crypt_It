from math import gcd
from secrets import randbelow
from typing import List, Tuple


class RSACipher:


    @staticmethod
    def gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b

        return a

 
    @staticmethod
    def modular_pow(base: int,exponent: int,modulus: int) -> int:
        result = 1
        base %= modulus

        while exponent > 0:
            if exponent & 1:
                result = (result * base) % modulus

            base = (base * base) % modulus
            exponent >>= 1

        return result


    @staticmethod
    def extended_gcd(a: int,b: int) -> Tuple[int, int, int]:

        if b == 0:
            return a, 1, 0

        gcd_value, x1, y1 = RSACipher.extended_gcd(
            b,
            a % b
        )

        x = y1
        y = x1 - (a // b) * y1

        return gcd_value, x, y


    @staticmethod
    def modular_inverse(a: int,modulus: int) -> int:

        gcd_value, x, _ = RSACipher.extended_gcd(
            a,
            modulus
        )

        if gcd_value != 1:
            raise ValueError(
                "Modular inverse does not exist."
            )

        return x % modulus



    @staticmethod
    def is_prime(number: int) -> bool:

        if number < 2:
            return False

        if number == 2:
            return True

        if number % 2 == 0:
            return False

        divisor = 3

        while divisor * divisor <= number:
            if number % divisor == 0:
                return False

            divisor += 2

        return True



    @staticmethod
    def generate_prime(minimum: int = 100,maximum: int = 40000) -> int:

        while True:
            candidate = randbelow(
                maximum - minimum + 1
            ) + minimum

            if RSACipher.is_prime(candidate):
                return candidate



    @staticmethod
    def generate_keys() -> Tuple[int, int, int]:

        p = RSACipher.generate_prime()
        q = RSACipher.generate_prime()

        while p == q:
            q = RSACipher.generate_prime()
        n = p * q
        phi = (p - 1) * (q - 1)
        e = 3
        while RSACipher.gcd(e, phi) != 1:
            e += 2
        d = RSACipher.modular_inverse(e, phi)
        return e, d, n



    @staticmethod
    def encrypt(text: str,e: int,n: int) -> List[int]:

        if n <= 255:
            raise ValueError(
                "RSA modulus n must be greater than 255."
            )
        result = []

        for character in text:
            value = ord(character)

            if value > 255:
                raise ValueError(
                    "RSA implementation supports only "
                    "characters with values from 0 to 255."
                )
            encrypted = RSACipher.modular_pow(
                value,
                e,
                n
            )
            result.append(encrypted)

        return result



    @staticmethod
    def decrypt(encrypted: List[int],d: int,n: int) -> str:

        result = []

        for value in encrypted:
            decrypted = RSACipher.modular_pow(
                value,
                d,
                n
            )
            if decrypted < 0 or decrypted > 255:
                raise ValueError(
                    "Invalid RSA decrypted value."
                )

            result.append(chr(decrypted))
        return "".join(result)