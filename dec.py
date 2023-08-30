from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import binascii
import ast

from cryptography.fernet import Fernet
import base64

import os

filename_org = input("what file do you want to read: ")
filename = "files/"+filename_org
key = input("Gib key:")
print("Lenth Check, if error make sure its 44:", len(key))

cipher_suite = Fernet(key)

# Import keys

priv = open("privatekey.txt", "rb")
keyPair = (priv.read())
keyPair = (cipher_suite.decrypt(keyPair))
keyPair = RSA.importKey(keyPair)
priv.close()

try:
    #try to read file, if file oversized goto except
    msgfile = open(filename, "rb")
    msg = (msgfile.read())
    msgfile.close()

    #try to decrypt
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = str(decryptor.decrypt(ast.literal_eval(str(msg))))[2:-1]
    decrypted = decrypted.replace("\\n", "\n")

    #print out decrypted message
    print(decrypted)
except:
    #try to open the encripted key that opens the file
    msgkey = open("files/OVERSIZEDKEY-"+filename_org, "rb")
    msgk = (msgkey.read())
    msgkey.close() 

    #decrypt the key(symetric) with asymetric encription
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = str(decryptor.decrypt(ast.literal_eval(str(msgk))))[2:-1]

    #open the symetrically encripted file
    msgfile = open("files/OVERSIZED-"+filename_org, "rb")
    msg = (msgfile.read())
    msgfile.close()

    #get the symetric key
    f = Fernet(decrypted)

    #unencript the file
    finalmsg = str(f.decrypt(msg))[2:-1]
    finalmsg = finalmsg.replace("\\n", "\n")

    #print out the file
    print(finalmsg)


