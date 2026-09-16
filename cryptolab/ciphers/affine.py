class AffineCipher:
    def encrypt(text :str, a: int,b:int)->str:
        if not isinstance(a, int) or not isinstance(b,int):
            raise TypeError("both keys must be an int")
            
        correct_as =  [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

        if a not in correct_as:
            raise ValueError('a must be coprime with 26, pick one from 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23 and 25')


        result = ''

        for char in text:
            if char.isupper():
                result += chr(((ord(char) - ord("A"))*a + b) % 26 + ord("A"))
            elif char.islower():
                result += chr(((ord(char) - ord("a"))*a + b) % 26 + ord("a"))
            else:
                result += char
            
        return result
    def decrypt(text :str, a: int,b:int) -> str:
        if not isinstance(a, int) or not isinstance(b,int):
            raise TypeError("both keys must be an int")
                    
        correct_as =  [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
        
        if a not in correct_as:
            raise ValueError('a must be coprime with 26, pick one from 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23 and 25')
        
        result = ''

        rev_a = pow(a,-1,26)
        
        for char in text:
            if char.isupper():
                result += chr(((ord(char) - ord("A")- b)*rev_a) % 26 + ord("A"))
            elif char.islower():
                result += chr(((ord(char) - ord("a")- b)*rev_a) % 26 + ord("a"))
            else:
                result += char
                    
        return result