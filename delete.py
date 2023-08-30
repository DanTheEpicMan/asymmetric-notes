from Crypto.PublicKey import RSA
from cryptography.fernet import Fernet
import base64
import os
import random
import time
import sys

filename_org = str(input("Filename: "))
filename = "files/"+filename_org

sys.set_int_max_str_digits(10*999)

try:
    with open(filename, 'rb') as file:
        textsize = int(len(file.read()))
except:
    #open the symetrically encripted file
    file = open("files/OVERSIZED-"+filename_org, "rb")
    textsize = int(len(file.read()))
    file.close()

    filename = "files/OVERSIZED-"+filename_org
    with open(filename, 'wb') as f:
        f.write(bytes(str(random.randrange(10**textsize, 10**(textsize+1))), "utf-8"))
    f.close()
    time.sleep(0.05)
    with open(filename, 'wb') as f:
        f.write(bytes(str(random.randrange(10**textsize, 10**(textsize+1))), "utf-8"))
    f.close()
    time.sleep(0.05)
    with open(filename, 'wb') as f:
        f.write(bytes(str(random.randrange(10**textsize, 10**(textsize+1))), "utf-8"))
    f.close()
    os.remove(filename)

    filename = "files/OVERSIZEDKEY-"+filename_org




with open(filename, 'wb') as f:
    f.write(bytes(str(random.randrange(10**textsize, 10**(textsize+1))), "utf-8"))
f.close()
time.sleep(0.05)
with open(filename, 'wb') as f:
    f.write(bytes(str(random.randrange(10**textsize, 10**(textsize+1))), "utf-8"))
f.close()
time.sleep(0.05)
with open(filename, 'wb') as f:
    f.write(bytes(str(random.randrange(10**textsize, 10**(textsize+1))), "utf-8"))
f.close()

time.sleep(0.05)

os.remove(filename)
