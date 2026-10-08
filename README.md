# Encryption POC

A simple Python proof-of-concept demonstrating **Fernet symmetric encryption and decryption of files** using the `cryptography` library.

This project was created for educational purposes to learn about file encryption, key generation, file handling, and cryptographic workflows.

> **IMPORTANT:** This program modifies files in its current working directory. Do **not** run it in a directory containing important or personal data. Use a dedicated disposable testing folder or authorized lab environment.

## Features

* Generates a Fernet encryption key
* Saves the key as `Thekey.key`
* Finds files in the current working directory
* Encrypts their contents using Fernet
* Provides a separate decryption program
* Restores encrypted file contents using the saved key
* Creates `Note.txt` with information about the encryption process

## Requirements

* Python 3.x
* `cryptography`

Install the dependency with:

```bash
pip install cryptography
```

## Files

```text
EncryptionPOC.py    # Encrypts files in the current directory
DecryptionPOC.py   # Decrypts files using Thekey.key
Thekey.key         # Generated encryption key
Note.txt           # Generated information note
```

## How It Works

### Encryption

`EncryptionPOC.py`:

1. Looks at files in the current working directory.
2. Ignores the POC scripts, key file, and note file.
3. Generates a new Fernet key.
4. Saves the key to `Thekey.key`.
5. Reads each selected file.
6. Encrypts its contents using Fernet.
7. Writes the encrypted contents back to the file.
8. Creates `Note.txt`.

### Decryption

`DecryptionPOC.py`:

1. Finds the encrypted files in the current working directory.
2. Loads `Thekey.key`.
3. Reads each encrypted file.
4. Decrypts its contents using the key.
5. Writes the decrypted contents back.
6. Removes `Note.txt` and `Thekey.key`.

## Safety Warning

**Do not run this program in your normal Documents, Desktop, Downloads, project, or system directories.**

The encryption program modifies files directly. Running it in the wrong directory can result in unwanted data modification or data loss.

For testing, create a dedicated disposable directory containing only files that you are willing to modify.

The encryption key is required for successful decryption. **Keep `Thekey.key` safe and do not delete it until you have successfully restored your test files.**

Do not run the encryption program repeatedly on already-encrypted files.

## Authorized Use

This project is intended for:

* Personal educational experiments
* Cybersecurity labs
* Controlled testing environments
* Systems and files that you own or have explicit permission to test

Unauthorized encryption or modification of someone else's data may be illegal.

The author does not authorize unauthorized use of this software.

## Disclaimer

This software is provided for educational purposes and **"as is"**, without warranties of any kind.

The author is not responsible for data loss, data modification, damage, or unauthorized use resulting from this software.

**Always test in an isolated, disposable environment and maintain backups of any data you care about.**

## Educational Purpose

This project demonstrates concepts including:

* Symmetric cryptography
* Fernet authenticated encryption
* Key generation and storage
* Python file I/O
* Directory/file handling with `os`
* Encryption/decryption workflows

This is an educational proof-of-concept and is **not intended to be used as ransomware or for unauthorized data encryption**.
