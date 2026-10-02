import pytest

from cryptit.ciphers.rsa import RSACipher


def test_gcd():
    assert RSACipher.gcd(48, 18) == 6
    assert RSACipher.gcd(17, 5) == 1


def test_modular_pow():
    assert RSACipher.modular_pow(2, 10, 1000) == 24
    assert RSACipher.modular_pow(5, 0, 26) == 1


def test_modular_inverse():
    assert RSACipher.modular_inverse(5, 26) == 21


def test_modular_inverse_does_not_exist():
    with pytest.raises(ValueError):
        RSACipher.modular_inverse(6, 26)


def test_is_prime():
    assert RSACipher.is_prime(2)
    assert RSACipher.is_prime(17)
    assert not RSACipher.is_prime(1)
    assert not RSACipher.is_prime(15)


def test_generate_keys():
    e, d, n = RSACipher.generate_keys()

    assert e > 1
    assert d > 1
    assert n > 255


def test_encrypt_decrypt():
    e, d, n = RSACipher.generate_keys()

    encrypted = RSACipher.encrypt(
        "hello",
        e,
        n
    )

    decrypted = RSACipher.decrypt(
        encrypted,
        d,
        n
    )

    assert decrypted == "hello"


def test_encrypt_returns_integers():
    e, _, n = RSACipher.generate_keys()

    encrypted = RSACipher.encrypt(
        "hello",
        e,
        n
    )

    assert all(isinstance(value, int) for value in encrypted)


def test_encrypt_rejects_small_modulus():
    with pytest.raises(ValueError):
        RSACipher.encrypt(
            "hello",
            3,
            255
        )


def test_encrypt_rejects_non_ascii_character():
    e, _, n = RSACipher.generate_keys()

    with pytest.raises(ValueError):
        RSACipher.encrypt(
            "ż",
            e,
            n
        )