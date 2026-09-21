# CryptoLab

```text
      :::::::: ::::::::: :::   ::::::::::::::::::::::::::::::: :::           :::    ::::::::: 
    :+:    :+::+:    :+::+:   :+::+:    :+:   :+:   :+:    :+::+:         :+: :+:  :+:    :+: 
   +:+       +:+    +:+ +:+ +:+ +:+    +:+   +:+   +:+    +:++:+        +:+   +:+ +:+    +:+  
  +#+       +#++:++#:   +#++:  +#++:++#+    +#+   +#+    +:++#+       +#++:++#++:+#++:++#+    
 +#+       +#+    +#+   +#+   +#+          +#+   +#+    +#++#+       +#+     +#++#+    +#+    
#+#    #+##+#    #+#   #+#   #+#          #+#   #+#    #+##+#       #+#     #+##+#    #+#     
######## ###    ###   ###   ###          ###    ######## #############     ############       
```

Educational cryptography toolkit written in Python.

## Project goals

CryptoLab is a command-line application for experimenting with classical cryptographic algorithms.

The project is primarily educational and focuses on understanding how different ciphers work and how they can be implemented and tested in Python.

## Current features

- Caesar cipher
- Vigenere cipher
- Affine cipher
- Hill cipher
- Playfair cipher
- Encryption and decryption
- Multiple cipher iterations
- Text input
- File input
- CLI argument validation
- Automated tests with pytest

## Planned features

- RSA
- Enigma

## Requirements

- Python >=3.10
- pytest

## Installation

Clone the repository and install the project dependencies.

```bash
git clone <repository-url>
cd CryptoLab
```

## Running

```bash
cryptolab [-h] --cipher {caesar,vigenere,affine,hill} [--key KEY] [--iterations ITERATIONS] (--text TEXT | --file FILE) [--decrypt] [--verbose]
```

## Examples

### Caesar

```bash
cryptolab --cipher caesar --key 3 --text "hello"
```

Decrypt:

```bash
cryptolab --cipher caesar --key 3 --text "khoor" --decrypt
```

### Vigenere

```bash
cryptolab --cipher vigenere --key secret --text "hello"
```

### Affine

```bash
cryptolab --cipher affine --key "5,8" --text "hello"
```

### Hill

2x2 matrix:

```bash
cryptolab --cipher hill --key "3,3;2,5" --text "hello"
```

3x3 matrix:

```bash
cryptolab --cipher hill --key "6,24,1;13,16,10;20,17,15" --text "hello"
```
### Playfair

```bash
cryptolab --cipher playfair --key MONARCHY --text "INSTRUMENTS"
```

Decrypt:

```bash
cryptolab --cipher playfair --key MONARCHY --text "GATLMZCLRQXA" --decrypt
```
## Cipher keys

- **Caesar** — key must be an integer.
- **Vigenere** — key must be a non-empty string containing only letters.
- **Affine** — key consists of two numbers in the format `"a,b"`. `a` must be coprime with 26.
- **Hill** — key must be a square matrix. Currently supported sizes are 2x2 and 3x3. The determinant must be invertible modulo 26.

Matrix formats:

```text
2x2: x,x;x,x

3x3: x,x,x;y,y,y;z,z,z
```

## File input

CryptoLab can process text files using the `--file` argument:

```bash
cryptolab --cipher caesar --key 3 --file input.txt
```

## Help

Display all available options:

```bash
cryptolab --help
```

## Tests

Run the test suite with:

```bash
pytest
```

## Project status

CryptoLab is an educational project under active development.

New ciphers, validation rules, tests and CLI features will be added over time.