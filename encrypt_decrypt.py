from cryptography.fernet import Fernet

message = str(input("Please enter the message : "))

key = Fernet.generate_key()

fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()

print("original string: ", message)
print("decrypted string: ", decMessage)


