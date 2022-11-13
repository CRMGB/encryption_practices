import io
import os
import unittest
from encryption import encrypt_file


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        # <-- absolute dir the script is in
        self.script_dir = os.path.dirname(__file__)
        self.file_to_encrypt = io.BytesIO()

class EncryptTestCase(BaseTestCase):
    def test_ensure_the_file_to_upload_is_encrypted_and_able_to_decrypt(self):
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

