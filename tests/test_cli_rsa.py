from cryptit.cli import (
    create_parser,
    validate_args,
    parse_rsa_key,
)


def test_rsa_accepts_valid_key():
    parser = create_parser()

    args = parser.parse_args([
        "--cipher", "rsa",
        "--key", "17,2753,3233",
        "--text", "hello"
    ])

    validate_args(parser, args)

    assert args.cipher == "rsa"
    assert args.key == "17,2753,3233"


def test_rsa_key_is_parsed_correctly():
    result = parse_rsa_key("17,2753,3233")

    assert result == (17, 2753, 3233)


def test_rsa_rejects_invalid_key_format():
    parser = create_parser()

    args = parser.parse_args([
        "--cipher", "rsa",
        "--key", "17,2753",
        "--text", "hello"
    ])

    try:
        validate_args(parser, args)
    except SystemExit as error:
        assert error.code == 2
    else:
        assert False, "Expected parser.error()"


def test_rsa_rejects_iterations():
    parser = create_parser()

    args = parser.parse_args([
        "--cipher", "rsa",
        "--key", "17,2753,3233",
        "--iterations", "2",
        "--text", "hello"
    ])

    try:
        validate_args(parser, args)
    except SystemExit as error:
        assert error.code == 2
    else:
        assert False, "Expected parser.error()"


def test_rsa_generate_keys_mode():
    parser = create_parser()

    args = parser.parse_args([
        "--cipher", "rsa",
        "--generate-keys"
    ])

    validate_args(parser, args)

    assert args.generate_keys is True
    assert args.cipher == "rsa"


def test_rsa_generate_keys_cannot_use_key():
    parser = create_parser()

    args = parser.parse_args([
        "--cipher", "rsa",
        "--generate-keys",
        "--key", "17,2753,3233"
    ])

    try:
        validate_args(parser, args)
    except SystemExit as error:
        assert error.code == 2
    else:
        assert False, "Expected parser.error()"