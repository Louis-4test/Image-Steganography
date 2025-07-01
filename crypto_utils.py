from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_text(text, key):
    f = Fernet(key)
    return f.encrypt(text.encode())

def decrypt_text(token, key):
    f = Fernet(key)
    return f.decrypt(token).decode()
