from cryptolab.ciphers.caesar import CaesarCipher

def test_encrypt_basic():
    result = CaesarCipher.encrypt("ABC", 3)

    assert result == "DEF"


def test_encrypt_lowercase():
    result = CaesarCipher.encrypt("abc", 3)

    assert result == "def"


def test_encrypt_uppercase():
    result = CaesarCipher.encrypt("XYZ", 3)

    assert result == "ABC"


def test_encrypt_mixed_case():
    result = CaesarCipher.encrypt("Hello", 3)

    assert result == "Khoor"


def test_encrypt_preserves_spaces_and_special_characters():
    result = CaesarCipher.encrypt("Hello, World!", 3)

    assert result == "Khoor, Zruog!"


def test_encrypt_preserves_numbers():
    result = CaesarCipher.encrypt("Hello 123", 3)

    assert result == "Khoor 123"


def test_encrypt_with_key_greater_than_alphabet():
    result = CaesarCipher.encrypt("ABC", 29)

    assert result == "DEF"


def test_encrypt_with_key_zero():
    result = CaesarCipher.encrypt("Hello World", 0)

    assert result == "Hello World"


def test_decrypt_basic():
    result = CaesarCipher.decrypt("DEF", 3)

    assert result == "ABC"


def test_decrypt_mixed_case():
    result = CaesarCipher.decrypt("Khoor Zruog", 3)

    assert result == "Hello World"


def test_decrypt_with_key_greater_than_alphabet():
    result = CaesarCipher.decrypt("DEF", 29)

    assert result == "ABC"


def test_encrypt_then_decrypt_returns_original_text():
    original = "Hello, World! 123"

    encrypted = CaesarCipher.encrypt(original, 7)
    decrypted = CaesarCipher.decrypt(encrypted, 7)

    assert decrypted == original

