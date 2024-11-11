import re

class vaidator:
    def __init__(self):
        pass

    def is_valid_email(self, email:str) -> bool:
        # Regular expression pattern for validating an Email
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def is_valid_password(self, password: str) -> bool:
        # Check for minimum length
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            return False
        # Check for at least one uppercase letter
        if not re.search(r'[A-Z]', password):
            print("Password must contain at least one uppercase letter.")
            return False
        # Check for at least one lowercase letter
        if not re.search(r'[a-z]', password):
            print("Password must contain at least one lowercase letter.")
            return False
        # Check for at least one digit
        if not re.search(r'[0-9]', password):
            print("Password must contain at least one digit.")
            return False
        # Check for at least one special character
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            print("Password must contain at least one special character.")
            return False
        # If all conditions are met
        return True

