# Define what the password is for
info = input("What is this password for?\n")

# Encrypt password
def encryption(password, position):
    encrypted_pass = password[position:] + password[:position]
    return encrypted_pass

# Get user password and encrypt it
def urs_pass_encrypt():
    encode_pass = input("Please input the password you want to encrypt:\n")
    encrypt_pass = encryption(encode_pass, 10)
    print("Encrypted password: {}\n".format(encrypt_pass))
    print("You can find the encrypted version in the specified text file!")

    # Open and write to the desired file the password
    with open(r"C:\Users\Radu\Desktop\Stuff\Notes\text.txt", "a") as file: # Replace with a specific text file path
        file.write("\n{} - {}".format(encrypt_pass, info))

urs_pass_encrypt()