import numpy as np
import re
from math import gcd
from string import ascii_lowercase

class HillCipher:
    @staticmethod
    def parse_key(text: str):
        matrix = np.array([[int(x) for x in row.split(",")] for row in text.split(";")],dtype = int)
        return matrix

    @staticmethod
    def validate_key(text: str) -> bool:
        pattern = r"^\d+(,\d+){1,2}(;\d+(,\d+){1,2}){1,2}$"
        if not re.fullmatch(pattern, text):
            return False
        matrix = HillCipher.parse_key(text)
        return matrix.shape in [(2, 2), (3, 3)]
    
    def encrypt(self, text: str, key: str) -> str:
        result =''
        alphabet = np.array(list(ascii_lowercase))
        if self.validate_key(key):
            matrix = self.parse_key(key)
            det = round(np.linalg.det(matrix))
            if gcd(det,26) == 1:
                shift = matrix.shape[0]
                fragments = []
                tmp=[]
                
                for i in text:
                    tmp.append(i)
                    if len(tmp)==shift:
                        np_fragment = np.array([np.where(alphabet == char)[0][0]for char in tmp], dtype=int)
                        tmp =[]
                        fragments.append(np_fragment)

                original_length = len(text)
                if tmp:
                    for i in range(shift - len(tmp)):
                        tmp.append('x')
                np_fragment = np.array([np.where(alphabet == char)[0][0] for char in tmp],dtype=int)
                fragments.append(np_fragment)

                for i in fragments:
                    result_fragment = i @ matrix
                    result_fragment = result_fragment % 26
                    letters_str = "".join(alphabet[result_fragment])
                    result += letters_str
                return result[:original_length]
            else:
                raise ValueError('determinant of the key must be invertible modulo 26')
        else:
            raise ValueError('matrix needs to be either square 2x2 or 3x3 provide values in e.g. x,x;x,x format')

    def decrypt(self, text: str, key: str) -> str:
        result = ''
        alphabet = np.array(list(ascii_lowercase))

        if self.validate_key(key):
            matrix = self.parse_key(key)
            det = round(np.linalg.det(matrix))
            shift = matrix.shape[0]

            if gcd(det, 26) == 1:
                det_mod = det % 26
                det_inv = pow(det_mod, -1, 26)

                if shift == 2:
                    a, b = matrix[0, 0], matrix[0, 1]
                    c, d = matrix[1, 0], matrix[1, 1]

                    adjugate = np.array([
                        [d, -b],
                        [-c, a]
                    ])

                elif shift == 3:
                    cofactors = np.zeros((3, 3), dtype=int)

                    for i in range(3):
                        for j in range(3):
                            sub = np.delete(
                                np.delete(matrix, i, axis=0),
                                j,
                                axis=1
                            )

                            sub_det = (
                                sub[0, 0] * sub[1, 1]
                                - sub[0, 1] * sub[1, 0]
                            )

                            cofactors[i, j] = ((-1) ** (i + j)) * sub_det

                    adjugate = cofactors.T

                inv_matrix = (det_inv * adjugate) % 26

                fragments = []
                tmp = []

                for char in text:
                    tmp.append(char)

                    if len(tmp) == shift:
                        np_fragment = np.array(
                            [np.where(alphabet == char)[0][0] for char in tmp],
                            dtype=int
                        )

                        tmp = []
                        fragments.append(np_fragment)

                original_length = len(text)

                if tmp:
                    for _ in range(shift - len(tmp)):
                        tmp.append('x')

                    np_fragment = np.array(
                        [np.where(alphabet == char)[0][0] for char in tmp],
                        dtype=int
                    )

                    fragments.append(np_fragment)

                for fragment in fragments:
                    result_fragment = fragment @ inv_matrix
                    result_fragment %= 26

                    letters_str = "".join(alphabet[result_fragment])
                    result += letters_str

                return result[:original_length]

            else:
                raise ValueError(
                    'determinant of the key must be invertible modulo 26'
                )

        else:
            raise ValueError(
                'matrix needs to be either square 2x2 or 3x3 '
                'provide values in e.g. x,x;x,x format'
            )