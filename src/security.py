class Security:
    def __init__(self):
        self.users = {
            "admin": {"role": "admin", "password": "password123"},
            "analyst": {"role": "analyst", "password": "password456"}
        }

    def authenticate_user(self, username, password):
        """
        Authenticates a user based on username and password.
        """
        user = self.users.get(username)
        if user and user["password"] == password:
            return True
        return False

    def two_factor_authentication(self, username):
        """
        Simulates a two-factor authentication process.
        """
        # In a real implementation, this would send a code to the user's
        # registered device.
        print(f"Sending 2FA code to the registered device for {username}...")
        return "2FA code sent."

    def authorize_user(self, username, required_role):
        """
        Authorizes a user based on their role.
        """
        user_role = self.users.get(username, {}).get("role")
        if user_role == required_role:
            return True
        return False
