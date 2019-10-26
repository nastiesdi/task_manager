import re


def is_valid_email(email):
    return True if re.search(r'[a-zA-Z0-9]@[a-z][.][a-z]', email) else False
