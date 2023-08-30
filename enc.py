from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import binascii
import ast

from cryptography.fernet import Fernet
import base64

#global text


def theEncrPart(text):

    filename = input("Provide the filename you want to save: ")
    filename_org = filename

    msg = text

    oversized = False
    oversized_path = ""
    if (len(msg) > 900):
        filename = "files/OVERSIZED-"+filename
        oversized = True
        oversized_path = "files/OVERSIZEDKEY-"+filename_org
    else:
        filename = "files/"+filename
    # Import keys
    pub = open("publickey.txt", "rb")
    pubKey = RSA.importKey(pub.read())
    pub.close()

    # --------------------------------------------------------------
    # encryption

    encryptor = PKCS1_OAEP.new(pubKey)

    if (oversized == True):
        from cryptography.fernet import Fernet
        fkey = Fernet.generate_key()
        f = Fernet(fkey)

        #encript file symetrically 
        file = open(filename, "wb")
        file.write(f.encrypt(bytes(msg, "utf-8")))
        file.close()

        #save the symetric key (fkey) using asymetric
        fencrypted = encryptor.encrypt(fkey)
        ferkey = open(oversized_path, "wb")
        ferkey.write(fencrypted)
        ferkey.close()
        print("""Note: your file exeds the max amount of charicters and will be encripted as OVERSIZED-filename useg symetric encription
        this means that asymetric encription will be used to secure the synetric key\nNO ACTION HAS TO BE TAKEN BY YOU, when decrypting the 
        file OVERSIZED- should NOT be added to the front of the filename""")
    else:
        encrypted = encryptor.encrypt(msg.encode())

        pub = open(filename, "wb")
        pub.write(encrypted)
        pub.close()

#from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QSizePolicy
import sys
from PySide2 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide2 Window")
        self.setGeometry(200, 100, 200, 100)

        self.label = QtWidgets.QLabel("Enter message to be encrypted:")

        self.text_field = QtWidgets.QTextEdit(self)
        self.text_field.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.WidgetWidth)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text_field)

        button = QtWidgets.QPushButton("Submit", self)
        button.clicked.connect(self.submit_text)
    
        self.layout.addWidget(button)

    def submit_text(self):
        text = self.text_field.toPlainText()
        #print(text)

        self.hide()
        theEncrPart(text)
        exit()


    def show(self):
        super().show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

print("Hello")