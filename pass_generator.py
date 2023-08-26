import random, array

# Password length
MAX_LEN = 16

# Numbers, letters, and characters for the password
NUMBERS = ['0', '1', '2', '3', '4',
           '5', '6', '7', '8', '9']

LOW_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
               'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'x', 'y', 'w', 'z']

UPPER_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                 'V', 'X', 'Y', 'W', 'Z']

SPECIAL_CHARS = ['!', '@', '#', '$', '%', '^', '&',
                 '*', '-', '_', '+', '=', '{', '}',
                 '[', ']', '|', '/', '<', '>', '?',
                 ':', ';', '~', '`', '\\']

# Combined array that holds all of the above arrays
COMBINED = NUMBERS + LOW_LETTERS + UPPER_LETTERS + SPECIAL_CHARS

# Generate a random number, letter, and special character
numbers = random.choice(NUMBERS)
lower_letters = random.choice(LOW_LETTERS)
upper_letters = random.choice(UPPER_LETTERS)
special_chars = random.choice(SPECIAL_CHARS)

# Initial password string
password = numbers + lower_letters + upper_letters + special_chars

for x in range(MAX_LEN - 4):
    password = password + random.choice(COMBINED)

# Empty string for the final form of the password
generated_password = ""
for x in password:
    # Add to generated_password character with number x
    generated_password = generated_password + x

# Print password
print("Generated password: {}\n".format(generated_password))