from cryptolab.ciphers.playfair import PlayfairCipher
import pytest


def test_create_matrix():
    cipher = PlayfairCipher()

    matrix = cipher._create_matrix("MONARCHY")

    assert len(matrix) == 5
    assert all(len(row) == 5 for row in matrix)
    assert matrix[0] == ["M", "O", "N", "A", "R"]


def test_prepare_text():
    cipher = PlayfairCipher()

    assert cipher._prepare_text("BALLOON") == "BALXLOON"
    assert cipher._prepare_text("HELLO") == "HELXLO"


def test_encrypt():
    cipher = PlayfairCipher()

    result = cipher.encrypt("INSTRUMENTS", "MONARCHY")

    assert result == "GATLMZCLRQXA"


def test_decrypt():
    cipher = PlayfairCipher()

    result = cipher.decrypt("GATLMZCLRQTX", "MONARCHY")

    assert result == "INSTRUMENTSZ"


def test_invalid_key():
    cipher = PlayfairCipher()

    with pytest.raises(ValueError, match="Key must contain only ASCII letters"):
        cipher.encrypt("HELLO", "key123")


def test_odd_ciphertext():
    cipher = PlayfairCipher()

    with pytest.raises(ValueError, match="Ciphertext length must be even"):
        cipher.decrypt("ABC", "MONARCHY")