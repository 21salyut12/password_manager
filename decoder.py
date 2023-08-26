import random, array

# Decrypt the password
def decryption(password, position):
    decrypted_pass = password[-position:] + password[:-position]
    return decrypted_pass

encrypted_pass = input("Please input the password you want to decrypt:\n")

# Decrypt and display the password
decrypted_pass = decryption(encrypted_pass, 10)
print("Decrypted password: {}\n".format(decrypted_pass))