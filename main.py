from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import binascii
import ast

from cryptography.fernet import Fernet
import base64

import subprocess

print("""
Note, Key makeing should be done only once and therefor 
is not included on this menu, the password used in that file
is imporatant and will be used when decripting

Encription will save the encripted text to file
Encript Message:    1
Decript Message:    2
Encript 4 Cloud:    3
Decrypt from Could: 4
Delete from disk:   5
Exit:               6

""")
choice = str(input("Choose: "))
if (choice == "1"):
    subprocess.run(["python", "enc.py"])
if (choice == "2"):
    subprocess.run(["python", "dec.py"])
if (choice == "3"):
    subprocess.run(["python", "cloud-encrypt.py"])
if (choice == "4"):
    subprocess.run(["python", "cloud-decrypt.py"])
if (choice == "5"):
    subprocess.run(["python", "delete.py"])
if (choice == "6"):
    exit
