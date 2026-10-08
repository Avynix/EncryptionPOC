from cryptography.fernet import Fernet
import os
files = []
ignored_files = ["EncryptionPOC.py", "DecryptionPOC.py", "Thekey.key", "Note.txt"]

for file in os.listdir():
    if file not in ignored_files and os.path.isfile(file):
        files.append(file)
    

print("Found the encrypted files.")
for file in files:
    print(file)

with open("Thekey.key", "rb") as thekey:
    secretkey = thekey.read()


for file in files:
    with open(file, "rb") as thefile:
        encrypted_content = thefile.read()
    decrypted_contents = Fernet(secretkey).decrypt(encrypted_content)
    with open(file, "wb") as thefile:
        thefile.write(decrypted_contents)

os.remove("Note.txt")
os.remove("Thekey.key")
