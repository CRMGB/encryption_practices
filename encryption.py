import io
from cryptography.fernet import Fernet

def generate_fernet_key():
    return Fernet.generate_key().decode("utf-8")

def encrypt_file(_f):
    file = _f.getvalue()
    fernet = Fernet(generate_fernet_key())
    encrypted = fernet.encrypt(file)
    return encrypted, fernet


def decrypt_file(file, crypto_key):
    file = bytes(file, "utf-8")
    fernet = Fernet(crypto_key)
    decrypted = fernet.decrypt(file)
    file_bytes = io.BytesIO(decrypted)
    return file_bytes
