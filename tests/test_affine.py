
import pytest

from cryptolab.ciphers.affine import AffineCipher


def test_encrypt():
    assert AffineCipher.encrypt("ABC", 5, 8) == "INS"


def test_decrypt():
    assert AffineCipher.decrypt("INS", 5, 8) == "ABC"


def test_encrypt_preserves_case():
    assert AffineCipher.encrypt("AbC", 5, 8) == "InS"


def test_encrypt_preserves_non_letters():
    assert AffineCipher.encrypt("Hello, World! 123", 5, 8) == "Rclla, Oaplx! 123"


def test_decrypt_preserves_non_letters():
    assert AffineCipher.decrypt("Rclla, Oaplx! 123", 5, 8) == "Hello, World! 123"


def test_encrypt_key_must_be_int():
    with pytest.raises(TypeError, match="both keys must be an int"):
        AffineCipher.encrypt("ABC", "5", 8)


def test_decrypt_key_must_be_int():
    with pytest.raises(TypeError, match="both keys must be an int"):
        AffineCipher.decrypt("INS", 5, "8")


def test_encrypt_a_must_be_coprime_with_26():
    with pytest.raises(ValueError, match="a must be coprime with 26"):
        AffineCipher.encrypt("ABC", 2, 8)


def test_decrypt_a_must_be_coprime_with_26():
    with pytest.raises(ValueError, match="a must be coprime with 26"):
        AffineCipher.decrypt("ABC", 2, 8)


def test_encrypt_with_negative_b():
    assert AffineCipher.encrypt("ABC", 5, -1) == "ZEJ"


def test_encrypt_with_b_greater_than_26():
    assert AffineCipher.encrypt("ABC", 5, 30) == "EJO"


def test_encrypt_decrypt_roundtrip():
    text = "Hello, CryptoLab! 123"
    encrypted = AffineCipher.encrypt(text, 5, 8)
    decrypted = AffineCipher.decrypt(encrypted, 5, 8)

    assert decrypted == text
