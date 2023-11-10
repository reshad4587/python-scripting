from hashlib import sha256
import os

def generate_salt():
    return os.urandom(16)

def hash_password(password, salt):
    hashed_password = sha256(password.encode('utf-8') + salt).hexdigest()
    return hashed_password, salt

def is_strong_password(password):
    return len(password) >= 8 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password)

try:
    while True:
        input_password = input("Enter a password: ")
        
        if is_strong_password(input_password):
            salt = generate_salt()
            hashed_password, salt = hash_password(input_password, salt)
            print(f"Hashed password: {hashed_password}")
            print(f"Salt: {salt.hex()}")
            break
        else:
            print("Weak password. Please choose a stronger password.")
            
except KeyboardInterrupt:
    print("\nExiting script!")


