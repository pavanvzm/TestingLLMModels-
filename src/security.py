import hashlib
import os

class Security:
    def __init__(self):
        self.roles = {
            "admin": ["read_logs", "generate_reports", "all"],
            "analyst": ["read_logs", "generate_reports"]
        }
        self.users = {
            "admin": {
                "role": "admin",
                "salt": os.urandom(16).hex(),
                "password_hash": ""
            },
            "analyst": {
                "role": "analyst",
                "salt": os.urandom(16).hex(),
                "password_hash": ""
            }
        }
        self.users["admin"]["password_hash"] = self._hash_password("password123", self.users["admin"]["salt"])
        self.users["analyst"]["password_hash"] = self._hash_password("password456", self.users["analyst"]["salt"])

    def _hash_password(self, password, salt):
        """Hashes the password with a salt."""
        salted_password = password.encode('utf-8') + salt.encode('utf-8')
        return hashlib.sha256(salted_password).hexdigest()

    def authenticate_user(self, username, password):
        """
        Authenticates a user based on username and password.
        """
        user = self.users.get(username)
        if user:
            password_hash = self._hash_password(password, user["salt"])
            if password_hash == user["password_hash"]:
                return True
        return False

    def two_factor_authentication(self, username):
        """
        Simulates a two-factor authentication process.
        """
        print(f"Sending 2FA code to the registered device for {username}...")
        return "123456"

    def verify_2fa_code(self, username, code):
        """
        Verifies the 2FA code.
        """
        return code == "123456"

    def authorize_user(self, username, required_permission):
        """
        Authorizes a user based on their permissions.
        """
        user_role = self.users.get(username, {}).get("role")
        if user_role:
            user_permissions = self.roles.get(user_role, [])
            if required_permission in user_permissions:
                return True
        return False
