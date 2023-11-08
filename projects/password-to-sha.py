from hashlib import sha256

input = input("Enter a password: ")
print(sha256(input.encode('utf-8')).hexdigest())