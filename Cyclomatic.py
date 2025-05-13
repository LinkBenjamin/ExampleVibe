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
    - Does NOT contain simple repeated patterns (e.g., 'abcabc', '123123', 'aaaaaa')
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

    # Check for repeated sequences (2-6 character sequences)
    for size in range(2, 7):
        for i in range(len(password) - 2 * size + 1):
            chunk = password[i:i+size]
            if chunk * 2 in password:
                return False

    # Check for any character repeated 4 or more times consecutively
    if re.search(r'(.)\1{3,}', password):
        return False

    return True
