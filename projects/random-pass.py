import string
import random

def generate_random_pass(length=8):
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(valid_characters) for i in range(length))
    return password

try:
    password_length_input = input("Enter the length of your password: ")

    if password_length_input:
        password_length = int(password_length_input)
    else:
        password_length = 8

    password = generate_random_pass(password_length)

    print(f"Generated password: {password}")

except ValueError:
    print("Please enter a valid number to define the length of the password.")