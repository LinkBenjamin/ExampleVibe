import re

def is_strong_password(password):
    """
    Validates the strength of a password with strict rules.
    
    Criteria:
    - At least 12 characters
    - Contains at least one lowercase letter
    - Contains at least one uppercase letter
    - Contains at least one digit
    - Contains at least one special character
    - No repeated substrings
    - No more than 2 identical characters in a row
    - No sequential patterns (abc, 123, etc.)
    - No common keyboard patterns
    """
    if len(password) < 12:
        return False

    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'\d', password):
        return False

    if not re.search(r'[!@#$%^&*()\-\_\+=]', password):
        return False

    # No identical characters repeated more than twice in a row
    if re.search(r'(.)\1{2,}', password):
        return False

    # Detect repeated substrings
    for size in range(2, len(password) // 2 + 1):
        for i in range(len(password) - 2 * size + 1):
            chunk = password[i:i + size]
            if chunk and password.count(chunk) > 1:
                return False

    # Detect sequential increasing or decreasing patterns (3+ chars)
    def has_sequence(s):
        for i in range(len(s) - 2):
            a, b, c = ord(s[i]), ord(s[i+1]), ord(s[i+2])
            if b - a == 1 and c - b == 1:  # increasing
                return True
            if a - b == 1 and b - c == 1:  # decreasing
                return True
        return False

    if has_sequence(password.lower()):
        return False

    # Disallow common keyboard patterns
    keyboard_patterns = ["qwerty", "asdf", "zxcv", "1234", "password", "admin"]
    for pattern in keyboard_patterns:
        if pattern in password.lower():
            return False

    return True
