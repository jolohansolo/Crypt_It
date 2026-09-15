import pytest
from argparse import Namespace

from cryptolab.cli import process_cipher
from cryptolab.ciphers.vigenere import VigenereCipher


class TestVigenereCipher:

    def test_encrypt(self):
        assert VigenereCipher.encrypt("HELLO", "KEY") == "RIJVS"

    def test_decrypt(self):
        assert VigenereCipher.decrypt("RIJVS", "KEY") == "HELLO"

    def test_encrypt_and_decrypt(self):
        text = "HELLOWORLD"
        key = "SECRET"

        encrypted = VigenereCipher.encrypt(text, key)
        decrypted = VigenereCipher.decrypt(encrypted, key)

        assert decrypted == text

    def test_repeating_key(self):
        assert VigenereCipher.encrypt("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR"

    def test_lowercase_text(self):
        assert VigenereCipher.encrypt("hello", "KEY") == "rijvs"

    def test_mixed_case_text(self):
        assert VigenereCipher.encrypt("Hello", "KEY") == "Rijvs"

    def test_key_is_case_insensitive(self):
        assert VigenereCipher.encrypt("HELLO", "KEY") == VigenereCipher.encrypt("HELLO", "key")

    def test_spaces_are_preserved(self):
        assert VigenereCipher.encrypt("HELLO WORLD", "KEY") == "RIJVS UYVJN"

    def test_special_characters_are_preserved(self):
        assert VigenereCipher.encrypt("HELLO, WORLD!", "KEY") == "RIJVS, UYVJN!"

    def test_numbers_are_preserved(self):
        assert VigenereCipher.encrypt("HELLO123", "KEY") == "RIJVS123"

    def test_empty_text(self):
        assert VigenereCipher.encrypt("", "KEY") == ""
        assert VigenereCipher.decrypt("", "KEY") == ""

    def test_single_character(self):
        assert VigenereCipher.encrypt("A", "KEY") == "K"
        assert VigenereCipher.decrypt("K", "KEY") == "A"

    def test_key_repeats_only_for_letters(self):
        assert VigenereCipher.encrypt("A A A", "KEY") == "K E Y"

    def test_decrypt_preserves_non_letters(self):
        assert VigenereCipher.decrypt("RIJVS, UYVJN!", "KEY") == "HELLO, WORLD!"

    def test_cli_uses_vigenere(self):
        args = Namespace(cipher="vigenere", key="KEY", iterations=1, decrypt=False)

        assert process_cipher(args, "HELLO") == "RIJVS"
