import random, array

# Decrypt the password
def decryption(password, position):
    decrypted_pass = password[-position:] + password[:-position]
    return decrypted_pass

# Read specified line from text file
def read_line(file_path, line_number):
    # Open and read file
    with open(file_path, "r") as file:
        # Read all the lines of the file
        lines = file.readlines()

        # Convert line_number to int 
        line_number = int(line_number)

        # If the number of the specified line is in the range of lines
        if line_number >= 0 and line_number < len(lines):
            # Return the content of the given line index
            return lines[line_number]
        else:
            return None

# Specify file path and line number to read       
file_path = "C:\\Users\\Radu\\Desktop\\Stuff\\Notes\\text.txt" # Replace with a specific text file path
line_number = input("Specify index of password: ")

# Read specified line from the file
line = read_line(file_path, line_number)

if line:
    # Split the line into encrypted password and info
    encrypted_pass, info = line.strip().split(" - ")

    # Decrypt the password
    decrypted_pass = decryption(encrypted_pass, 10)

    print("Encrypted password: {}\n".format(line))
    print("Decrypted password: {}\n".format(decrypted_pass))
else:
    print("Index out of range.")