# -*- coding: utf-8 -*-
"""Text encryption and  decryption.ipynb


#**Text encryption and decryption**
"""

from cryptography.fernet import Fernet


message = "Task 1 of Python Devloper Internship With Merishot"

key = Fernet.generate_key()

fernet = Fernet(key)

encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)
