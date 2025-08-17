import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.security import Security

class TestSecurity(unittest.TestCase):

    def setUp(self):
        self.security = Security()

    def test_authenticate_user_success(self):
        self.assertTrue(self.security.authenticate_user("admin", "password123"))

    def test_authenticate_user_failure(self):
        self.assertFalse(self.security.authenticate_user("admin", "wrongpassword"))

    def test_two_factor_authentication(self):
        self.assertEqual(self.security.two_factor_authentication("admin"), "123456")

    def test_verify_2fa_code_success(self):
        self.assertTrue(self.security.verify_2fa_code("admin", "123456"))

    def test_verify_2fa_code_failure(self):
        self.assertFalse(self.security.verify_2fa_code("admin", "654321"))

    def test_authorize_user_success(self):
        self.assertTrue(self.security.authorize_user("admin", "all"))

    def test_authorize_user_failure(self):
        self.assertFalse(self.security.authorize_user("analyst", "all"))

if __name__ == '__main__':
    unittest.main()
