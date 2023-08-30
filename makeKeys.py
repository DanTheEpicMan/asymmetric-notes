from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import binascii
import ast

from cryptography.fernet import Fernet
import base64

key = input("Gib key:")
print("Lenth Check, if error make sure its 44:", len(key))

cipher_suite = Fernet(key)

# key generation
keyPair = RSA.generate(8192)
pubKey = keyPair.publickey()
# --------------------------------------------------------------

# Export keys
pub = open("publickey.txt", "wb")
pub.write(pubKey.exportKey('PEM'))
pub.close()

encoded_text = (cipher_suite.encrypt(keyPair.exportKey('PEM')))
priv = open("privatekey.txt", "wb")
priv.write(encoded_text)
priv.close()