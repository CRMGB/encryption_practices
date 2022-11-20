import io
from cryptography.fernet import Fernet
import cryptacular.bcrypt


def encrypt_file(_f, fernet):
    """We use the Fernet key to encrypt the file"""
    try:
        file = _f.getvalue()
        key = Fernet(fernet)
        encrypted = key.encrypt(file)
    except Exception as e:
        print("Couldn't encrypt the file,", str(e))
        raise Exception(f"Couldn't encrypt the file {str(e)}")
    return encrypted, key

def decrypt_file(file, crypto_key):
    """Use the same Fernet in the encryption"""
    try:
        file = bytes(file, "utf-8")
        fernet = Fernet(crypto_key)
        decrypted = fernet.decrypt(file)
        file_bytes = io.BytesIO(decrypted)
        print("\nThe file has been succesfully decrypted")
    except Exception as e:
        raise Exception(f"{str(e)}, Unsuccessfully decrypted")
    return file_bytes

def hashing_and_salted_pass(passwrord):
    crypt = cryptacular.bcrypt.BCRYPTPasswordManager()
    encrypted = crypt.encode(passwrord)
    return encrypted