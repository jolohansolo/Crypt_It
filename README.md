```text
    :::::::: ::::::::: :::   ::::::::::::::::::::::::::::::::::::::::::::: 
  :+:    :+::+:    :+::+:   :+::+:    :+:   :+:        :+:        :+:      
 +:+       +:+    +:+ +:+ +:+ +:+    +:+   +:+         +:+        +:+      
  +#+       +#++:++#:   +#++:  +#+   +#+   +#+         +#+        +#+        
 +#+       +#+    +#+   +#+   +#+          +#+         +#+        +#+       
#+#    #+# #+#    #+#   #+#   #+#           #+#         #+#        #+#        
######## ###    ###   ###   ###             ###    ###########    ###        
```

Educational cryptography toolkit written in Python.

## Project goals

CryptIt is a command-line application for experimenting with classical and public-key cryptographic algorithms.

The project is primarily educational and focuses on understanding how different ciphers work and how they can be implemented and tested in Python.

## Current features

- Caesar cipher
- Vigenere cipher
- Affine cipher
- Hill cipher
- Playfair cipher
- RSA
- Encryption and decryption
- Multiple cipher iterations
- Text input
- File input
- RSA key pair generation
- RSA key saving
- CLI argument validation
- Automated tests with pytest

## Planned features

- Enigma

## Requirements

- Python >=3.10
- pytest

## Installation

Clone the repository and install CryptIt in editable mode.

```bash
git clone https://github.com/jolohansolo/Crypt_It.git
cd CryptIt
pip install -e .
```

For development and testing, install the test dependencies as well:

```bash
pip install pytest
```

## Running

```bash
cryptit [-h] --cipher {caesar,vigenere,affine,hill,playfair,rsa}
        [--key KEY] [--generate-keys] [--iterations ITERATIONS]
        [--text TEXT | --file FILE] [--decrypt] [--verbose]
```

## Examples

### Caesar

```bash
cryptit --cipher caesar --key 3 --text "hello"
```

Decrypt:

```bash
cryptit --cipher caesar --key 3 --text "khoor" --decrypt
```

### Vigenere

```bash
cryptit --cipher vigenere --key secret --text "hello"
```

### Affine

```bash
cryptit --cipher affine --key "5,8" --text "hello"
```

### Hill

2x2 matrix:

```bash
cryptit --cipher hill --key "3,3;2,5" --text "hello"
```

3x3 matrix:

```bash
cryptit --cipher hill --key "6,24,1;13,16,10;20,17,15" --text "hello"
```

### Playfair

```bash
cryptit --cipher playfair --key MONARCHY --text "INSTRUMENTS"
```

Decrypt:

```bash
cryptit --cipher playfair --key MONARCHY --text "GATLMZCLRQXA" --decrypt
```

### RSA

RSA does not support multiple iterations.

Encrypt text using a manually supplied RSA key:

```bash
cryptit --cipher rsa --key "e,d,n" --text "hello"
```

Decrypt RSA ciphertext:

```bash
cryptit --cipher rsa --key "e,d,n" --text "encrypted_values" --decrypt
```

RSA ciphertext is represented as comma-separated integer values.

### RSA key generation

Generate a new RSA key pair:

```bash
cryptit --cipher rsa --generate-keys
```

The generated keys are saved to:

```text
cryptit_rsa_keys.txt
```

The file contains the public key, private key, and the full CryptIt key format:

```text
e,d,n
```

The generated public key consists of:

```text
e
n
```

The generated private key consists of:

```text
d
n
```

## Cipher keys

- **Caesar** — key must be an integer.
- **Vigenere** — key must be a non-empty string containing only letters.
- **Affine** — key consists of two numbers in the format `"a,b"`. `a` must be coprime with 26.
- **Hill** — key must be a square matrix. Currently supported sizes are 2x2 and 3x3. The determinant must be invertible modulo 26.
- **Playfair** — key must be a non-empty string.
- **RSA** — key must contain three positive integers in the format `"e,d,n"`.

Matrix formats:

```text
2x2: x,x;x,x

3x3: x,x,x;y,y,y;z,z,z
```

## RSA

RSA is implemented as a public-key cryptosystem.

CryptIt supports:

- RSA key pair generation
- RSA encryption
- RSA decryption
- Manually supplied RSA keys
- Saving generated keys to a text file

The RSA key format used by CryptIt is:

```text
e,d,n
```

For encryption, CryptIt uses the public exponent `e` and modulus `n`.

For decryption, CryptIt uses the private exponent `d` and modulus `n`.

RSA key generation can be performed independently with:

```bash
cryptit --cipher rsa --generate-keys
```

RSA does not support the `--iterations` option.

## File input

CryptIt can process text files using the `--file` argument:

```bash
cryptit --cipher caesar --key 3 --file input.txt
```

RSA can also process text files:

```bash
cryptit --cipher rsa --key "e,d,n" --file input.txt
```

## Help

Display all available options:

```bash
cryptit --help
```

## Tests

Run the test suite with:

```bash
pytest
```
```

