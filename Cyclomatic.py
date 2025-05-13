import re

def is_strong_password(password):
    """
    Validates the strength of a password.
    
    Returns True if the password meets all of the following:
    - At least 8 characters
    - Contains at least one lowercase letter
    - Contains at least one uppercase letter
    - Contains at least one digit
    - Contains at least one special character
    """
    if len(password) < 8:
        return False
    
    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'\d', password):
        return False

    if not re.search(r'[!@#$%^&*()\-\_\+=]', password):
        return False

    return True
