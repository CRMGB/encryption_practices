import io
from cryptography.fernet import Fernet

def generate_fernet_key():
    """Generate fernet key and return it as a utf-8 string."""
    return Fernet.generate_key().decode("utf-8")

def encrypt_file(_f):
    """We use the Fernet key to encrypt the file"""
    try:
        file = _f.getvalue()
        fernet = Fernet(generate_fernet_key())
        encrypted = fernet.encrypt(file)
    except Exception as e:
        print("Couldn't encrypt the file,", str(e))
        raise Exception(f"Couldn't encrypt the file {str(e)}")
    return encrypted, fernet

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
