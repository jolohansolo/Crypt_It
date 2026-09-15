class CaesarCipher:
    @staticmethod
    def encrypt(text: str, key: int) -> str:
        result = ""

        for char in text:
            if char.isupper():
                result += chr((ord(char) - ord("A") + key) % 26 + ord("A"))
            elif char.islower():
                result += chr((ord(char) - ord("a") + key) % 26 + ord("a"))
            else:
                result += char

        return result

    @staticmethod
    def decrypt(text: str, key: int) -> str:
        return CaesarCipher.encrypt(text, -key)
