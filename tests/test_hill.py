import pytest

from cryptolab.ciphers.hill import HillCipher


def test_parse_key_2x2():
    matrix = HillCipher.parse_key("3,3;2,5")

    assert matrix.tolist() == [
        [3, 3],
        [2, 5]
    ]


def test_parse_key_3x3():
    matrix = HillCipher.parse_key("6,24,1;13,16,10;20,17,15")

    assert matrix.tolist() == [
        [6, 24, 1],
        [13, 16, 10],
        [20, 17, 15]
    ]


def test_validate_key_valid_2x2():
    assert HillCipher.validate_key("3,3;2,5") is True


def test_validate_key_valid_3x3():
    assert HillCipher.validate_key(
        "6,24,1;13,16,10;20,17,15"
    ) is True


def test_decrypt_2x2():
    cipher = HillCipher()

    result = cipher.decrypt("tc", "3,3;2,5")

    assert result == "nd"


def test_decrypt_3x3():
    cipher = HillCipher()

    result = cipher.decrypt(
        "pohe",
        "6,24,1;13,16,10;20,17,15"
    )

    assert result == "plgk"


def test_decrypt_non_invertible_key():
    cipher = HillCipher()

    with pytest.raises(
        ValueError,
        match="determinant of the key must be invertible modulo 26"
    ):
        cipher.decrypt("hello", "2,4;2,4")


def test_decrypt_preserves_original_length():
    cipher = HillCipher()

    result = cipher.decrypt("abc", "3,3;2,5")

    assert len(result) == 3
