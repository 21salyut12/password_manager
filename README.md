# Password Manager

Welcome to the Password Manager project!

## Description

This project is developed using Python and consists of two separate scripts. The primary purpose of this project is to provide a simple password management solution. It involves generating, randomizing, encrypting, and storing passwords securely in a text file. The project also includes a decryption process to retrieve the original password for authentication.

## Features

- Password Generation: The first script generates a random password with specified constraints, including length and character types.
- Encryption: The randomized password is encrypted using a simple form of Caesar's Cipher technique.
- File Storage: The encrypted password is stored in a text file along with a user-provided description.
- Password Retrieval: The second script reads the encrypted password from the text file.
- Decryption: The second script decrypts the password, providing the original password for user authentication.

## Usage

1. Run the `encoder.py` script to generate, randomize, encrypt, and store a password.
2. Run the `decoder.py` script to retrieve and decrypt the stored password.

## Validation Rules

The password format follows these simple validation rules:
- The password does not contain single or double quotes.
- The password does not contain spaces.

## How to Run

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the `encoder.py` script to generate and store a password.
4. Run the `decoder.py` script to retrieve and authenticate the password.

## Disclaimer

Please note that this project is intended for educational and personal use. Always follow best practices for password security and consider using established password management tools for sensitive information.

Feel free to explore, modify, and use this project as a starting point for your own password management solutions!


## Demonstration on how the project works
![](https://github.com/21salyut12/password_manager/blob/main/demo_password_manager.jpg)
