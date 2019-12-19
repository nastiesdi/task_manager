import re


def is_valid_email(email):
    return True if re.match(r'^([0-9a-zA-Z]+@+[a-z]+.+[a-z])$', email) else False


def is_valid_password(password):
    return True if re.match(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$', password) else False


def is_valid_age(age):
    return 15 < age < 100


def is_valid_name(name):
    if isinstance(name, str):
        return True if name.isalpha() and 2 < len(name) < 15 else False
    return False
