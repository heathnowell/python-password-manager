# Python Password Manager

A simple local password manager built in Python that stores credentials in an encrypted JSON file.

The project uses **Fernet symmetric encryption** to encrypt stored passwords and **bcrypt** to verify the master password.

## Features

- Add and store account credentials
- Encrypt passwords before saving them
- Decrypt saved passwords when viewing them
- Remove individual saved credentials
- Delete the local password file
- Verify access using a bcrypt-hashed master password
- Store credentials locally in `passwords.json`

## Technologies Used

- Python
- `cryptography` / Fernet
- `bcrypt`
- JSON file storage

## How It Works

The program asks the user to authenticate with a master password before accessing stored credentials.

After authentication, the user provides a Fernet encryption key. That key is used to encrypt passwords before they are written to `passwords.json` and to decrypt them when they are retrieved.

The master password itself is not stored in plaintext. The program verifies it against a bcrypt hash.

## Repository Structure

```text
python-password-manager/
├── .gitignore
├── README.md
├── password_manager.py
└── requirements.txt
```

`passwords.json` should remain local and should not be committed to GitHub.

## Requirements

- Python 3
- cryptography
- bcrypt

Install the required packages with:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
cryptography
bcrypt
```

## Running the Program

From the repository folder, run:

```bash
python password_manager.py
```

Follow the terminal prompts to authenticate, provide the encryption key, and use the password manager.

## Security Notes

This project was built as a learning project and is **not intended to replace a production password manager**.

Important considerations:

- Never commit real passwords or `passwords.json` to GitHub.
- Never publish a real Fernet key.
- The current project expects the encryption key to be provided by the user rather than deriving it from the master password.
- A production implementation would use more robust key management and additional security protections.

## What I Learned

This project helped me practice:

- Encrypting and decrypting data in Python
- Password hashing and authentication with bcrypt
- Reading and writing JSON data
- Managing local credential storage
- Working with third-party Python security libraries
- Designing a simple command-line workflow

## Possible Future Improvements

- Use `getpass` so the master password is hidden while typing
- Improve encryption-key management
- Support multiple accounts with the same username
- Add stronger input validation and error handling
- Add a graphical user interface
- Add automated tests
