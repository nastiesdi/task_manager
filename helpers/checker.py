import re


def check_priority(priority):
    return True if isinstance(priority, int) and 0 < priority < 6 else 'Priority is invalid'


def is_valid_email(email):
    return True if re.search(r'[a-zA-Z0-9]@[a-z][.][a-z]', email) else False
