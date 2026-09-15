import pytest

from cryptolab.cli import main


# ---------------------------------------------------------
# ENCRYPTION
# ---------------------------------------------------------

def test_cli_encrypt(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "cryptolab",
            "--cipher", "caesar",
            "--key", "3",
            "--text", "Hello World",
        ],
    )

    main()

    captured = capsys.readouterr()

    assert captured.out.strip() == "Khoor Zruog"


# ---------------------------------------------------------
# DECRYPTION
# ---------------------------------------------------------

def test_cli_decrypt(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "cryptolab",
            "--cipher", "caesar",
            "--key", "3",
            "--decrypt",
            "--text", "Khoor Zruog",
        ],
    )

    main()

    captured = capsys.readouterr()

    assert captured.out.strip() == "Hello World"


# ---------------------------------------------------------
# ITERATIONS
# ---------------------------------------------------------

def test_cli_iterations(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "cryptolab",
            "--cipher", "caesar",
            "--key", "3",
            "--iterations", "2",
            "--text", "ABC",
        ],
    )

    main()

    captured = capsys.readouterr()

    assert captured.out.strip() == "GHI"


# ---------------------------------------------------------
# VERBOSE
# ---------------------------------------------------------

def test_cli_verbose(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "cryptolab",
            "--cipher", "caesar",
            "--key", "3",
            "--text", "Hello",
            "--verbose",
        ],
    )

    main()

    captured = capsys.readouterr()

    assert "Cipher: caesar" in captured.out
    assert "Key: 3" in captured.out
    assert "Iterations: 1" in captured.out
    assert "Decrypt: False" in captured.out
    assert "Khoor" in captured.out


# ---------------------------------------------------------
# ARGUMENT VALIDATION
# ---------------------------------------------------------

def test_cli_requires_key(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "cryptolab",
            "--cipher", "caesar",
            "--text", "Hello",
        ],
    )

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 2

    captured = capsys.readouterr()

    assert "--cipher caesar requires --key" in captured.err


def test_cli_iterations_must_be_positive(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "cryptolab",
            "--cipher", "caesar",
            "--key", "3",
            "--iterations", "0",
            "--text", "Hello",
        ],
    )

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 2

    captured = capsys.readouterr()

    assert "iterations must be greater than 0" in captured.err


# ---------------------------------------------------------
# INPUT VALIDATION
# ---------------------------------------------------------

def test_cli_requires_text_or_file(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "cryptolab",
            "--cipher", "caesar",
            "--key", "3",
        ],
    )

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 2


def test_cli_does_not_allow_text_and_file_together(
    capsys,
    monkeypatch,
    tmp_path,
):
    test_file = tmp_path / "input.txt"
    test_file.write_text("Hello", encoding="utf-8")

    monkeypatch.setattr(
        "sys.argv",
        [
            "cryptolab",
            "--cipher", "caesar",
            "--key", "3",
            "--text", "Hello",
            "--file", str(test_file),
        ],
    )

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 2


# ---------------------------------------------------------
# FILE INPUT
# ---------------------------------------------------------

def test_cli_encrypt_file(capsys, monkeypatch, tmp_path):
    test_file = tmp_path / "input.txt"
    test_file.write_text("Hello World", encoding="utf-8")

    monkeypatch.setattr(
        "sys.argv",
        [
            "cryptolab",
            "--cipher", "caesar",
            "--key", "3",
            "--file", str(test_file),
        ],
    )

    main()

    captured = capsys.readouterr()

    assert captured.out.strip() == "Khoor Zruog"