# -*- coding: utf-8 -*-
"""HERITIER_UMUHIRE_25011575_.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JEA6ZoTimnmgNLgJZaCYXmQ5FbRQJ5Q8
"""

from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
message=b"UMUHIRE Heritier"
encrypted_message = f.encrypt(message)
output=f.decrypt(encrypted_message).decode()

print ("Original message:\t",message.decode(),"\nencrypted Message:\t",encrypted_message.decode(),"\ndecrypted message:\t",output)