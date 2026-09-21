class VigenereCipher:
    @staticmethod
    def encrypt(text: str, key: str) -> str:
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        
        if not key:
            raise ValueError("Key cannot be empty")
        
        if not key.isascii() or not key.isalpha():
            raise ValueError("Key must contain only letters")
        
        result = ''
        key = key.lower()
        key_index = 0

        for char in text:
            if char.isalpha():
                if char.isupper():
                    start = ord('A')
                else: 
                    start = ord('a')
                
                shift = ord(key[key_index % len(key)]) - ord("a")

                new_char = chr((ord(char) - start + shift) % 26 + start)
                result+=new_char

                key_index += 1
            else:
                result+=char

        return result

    @staticmethod
    def decrypt(text: str, key: str) -> str:
        if not isinstance(key, str):
            raise TypeError("Key must be a string")

        if not key:
            raise ValueError("Key cannot be empty")

        if not key.isascii() or not key.isalpha():
            raise ValueError("Key must contain only letters")
        
        result = ''
        key = key.lower()
        key_index = 0        
        for char in text:
            if char.isalpha():
                if char.isupper():
                    start = ord('A')
                else: 
                    start = ord('a')
                        
                shift = (ord(key[key_index % len(key)]) - ord("a"))*-1
        
                new_char = chr((ord(char) - start + shift) % 26 + start)
                result+=new_char
        
                key_index += 1
            else:
                result+=char
        
        return result
