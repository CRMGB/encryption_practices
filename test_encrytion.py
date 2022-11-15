import io
import os
import unittest
from . import encrypt_file, decrypt_file


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        # <-- absolute dir the script is in
        self.script_dir = os.path.dirname(__file__)        
        self.file_to_encrypt = io.BytesIO()

class EncryptTestCase(BaseTestCase):
    def test_ensure_the_file_to_upload_is_encrypted_and_able_to_decrypt(self):
        """Expect the file file uploaded is encrypted.
        Also expect the file is decrypted when we call the decrypt_file method.
        """
        # Read example file
        rel_path = "test_files/test_file_1.txt"
        abs_file_path = os.path.join(self.script_dir, rel_path)
        
        with open(abs_file_path, "rb") as f:
            data = f.read()  # Read the bytes of the input file
        for chunk in data:
            self.file_to_encrypt.write(bytes(chunk))
        f.close()
        output, fernet = encrypt_file(self.file_to_encrypt)
        # If text is encrypted it should allow you to decrypt
        self.assertTrue(fernet.decrypt(output), None)
        # Now check we can decrypt with our method
        file_decrypted = decrypt_file(output.decode(), fernet)
        # this time the file is decrypted so if we try to decrypt again will raise error
        with self.assertRaises(Exception):
            self.assertFalse(file_decrypted.decrypt(output), None)
