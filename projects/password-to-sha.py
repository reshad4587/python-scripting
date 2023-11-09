from hashlib import sha256
import os

def generate_salt():
    return os.urandom(16)

def hash_password(password, salt):
    hashed_password = sha256(password.encode('utf-8') + salt).hexdigest()
    return hashed_password, salt

try:
    input_password = input("Enter a password: ")
    salt = generate_salt()
    hashed_password, salt = hash_password(input_password, salt)
    print(f"Hashed password: {hashed_password}")
    print(f"Salt: {salt}")
    
except KeyboardInterrupt:
    print("\nExiting script!")


