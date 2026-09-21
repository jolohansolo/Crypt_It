class PlayfairCipher:

    @staticmethod
    def _create_matrix(key: str) -> list[list[str]]:
        key = key.upper().replace("J", "I")
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        matrix_string = ""

        for char in key + alphabet:
            if char not in matrix_string:
                matrix_string += char

        return [
            list(matrix_string[i:i + 5])
            for i in range(0, 25, 5)
        ]

    @staticmethod
    def _prepare_text(text: str) -> str:
        text = "".join(
            c.upper() for c in text if c.isalpha()
        ).replace("J", "I")

        prepared = ""

        i = 0
        while i < len(text):
            char1 = text[i]

            if i + 1 < len(text):
                char2 = text[i + 1]

                if char1 == char2:
                    prepared += char1 + "X"
                    i += 1
                else:
                    prepared += char1 + char2
                    i += 2
            else:
                prepared += char1 + "X"
                i += 1

        return prepared

    @staticmethod
    def _find_position(
        matrix: list[list[str]],
        char: str
    ) -> tuple[int, int]:

        for row in range(5):
            for col in range(5):
                if matrix[row][col] == char:
                    return row, col

        raise ValueError(
            f"Character {char} not found in matrix"
        )

    @staticmethod
    def encrypt(text: str, key: str) -> str:
        if not key.isascii() or not key.isalpha():
            raise ValueError(
                "Key must contain only ASCII letters"
            )

        matrix = PlayfairCipher._create_matrix(key)
        prepared_text = PlayfairCipher._prepare_text(text)

        result = ""

        for i in range(0, len(prepared_text), 2):
            char1 = prepared_text[i]
            char2 = prepared_text[i + 1]

            r1, c1 = PlayfairCipher._find_position(
                matrix, char1
            )
            r2, c2 = PlayfairCipher._find_position(
                matrix, char2
            )

            if r1 == r2:
                result += matrix[r1][(c1 + 1) % 5]
                result += matrix[r2][(c2 + 1) % 5]

            elif c1 == c2:
                result += matrix[(r1 + 1) % 5][c1]
                result += matrix[(r2 + 1) % 5][c2]

            else:
                result += matrix[r1][c2]
                result += matrix[r2][c1]

        return result

    @staticmethod
    def decrypt(text: str, key: str) -> str:
        if not key.isascii() or not key.isalpha():
            raise ValueError(
                "Key must contain only ASCII letters"
            )

        matrix = PlayfairCipher._create_matrix(key)

        text = "".join(
            c.upper() for c in text if c.isalpha()
        )

        if len(text) % 2 != 0:
            raise ValueError(
                "Ciphertext length must be even"
            )

        result = ""

        for i in range(0, len(text), 2):
            char1 = text[i]
            char2 = text[i + 1]

            r1, c1 = PlayfairCipher._find_position(
                matrix, char1
            )
            r2, c2 = PlayfairCipher._find_position(
                matrix, char2
            )

            if r1 == r2:
                result += matrix[r1][(c1 - 1) % 5]
                result += matrix[r2][(c2 - 1) % 5]

            elif c1 == c2:
                result += matrix[(r1 - 1) % 5][c1]
                result += matrix[(r2 - 1) % 5][c2]

            else:
                result += matrix[r1][c2]
                result += matrix[r2][c1]

        return result