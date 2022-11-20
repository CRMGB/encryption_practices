import io
import os
import unittest
from cryptacular.bcrypt import BCRYPTPasswordManager
from cryptography.fernet import Fernet
from encryption import encrypt_file, decrypt_file, hashing_and_salted_pass


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        # <-- absolute dir the script is in
        self.script_dir = os.path.dirname(__file__)        
        self.file_to_encrypt = io.BytesIO()
        

class EncryptTestCase(BaseTestCase):
    def generate_fernet_key(self):
        """Generate fernet key and return it as a utf-8 string."""
        return Fernet.generate_key().decode("utf-8")
    
    def read_file(self):
        # Read example file
        rel_path = "test_files/test_file_1.txt"
        abs_file_path = os.path.join(self.script_dir, rel_path)
        
        with open(abs_file_path, "rb") as f:
            data = f.read()  # Read the bytes of the input file
        for chunk in data:
            self.file_to_encrypt.write(bytes(chunk))
        f.close()
        
    def test_ensure_the_file_to_upload_is_encrypted(self):
        """Expect the file file uploaded is encrypted.
        Also expect the file is decrypted when we call the decrypt_file method.
        """
        fernet = self.generate_fernet_key()
        self.read_file()
        output, fernet = encrypt_file(self.file_to_encrypt, fernet)
        # If text is encrypted it should allow you to decrypt
        self.assertTrue(fernet.decrypt(output), None)

    def test_ensure_we_can_decrypt_the_file(self):
        fernet = self.generate_fernet_key()
        self.read_file()
        output, _ = encrypt_file(self.file_to_encrypt, fernet)
        # Now check we can decrypt with our method
        file_decrypted = decrypt_file(output.decode(), fernet)
        # this time the file is decrypted so if we try to decrypt again will raise error
        with self.assertRaises(Exception):
            self.assertFalse(file_decrypted.decrypt(output), None)
            
    def test_ensure_we_hash_pass_and_encrypt(self):
        pass_1 = "abcdef_12345"
        manager = BCRYPTPasswordManager()
        hashed = hashing_and_salted_pass(pass_1)
        hashed_2 = hashing_and_salted_pass(pass_1)
        self.assertNotEqual(hashed, hashed_2)
        self.assertTrue(manager.check(hashed, 'abcdef_12345'))
