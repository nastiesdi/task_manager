import re


def is_valid_email(email):
    return True if re.search(r'[a-z]@[a-z].', email) else False
    # return True if re.search(r'[a-zA-Z0-9]@[a-z][.][a-z]', email) else False


def is_valid_password(password):
    return True if len(password) > 5 else False
#rabotaet tolko s etim ysloviem


def is_valid_age(age):
    return True if 16 < age < 100 else False


def is_valid_name(name):
    if type(name) == str:
        return True if bool(re.match("^[A-Za-z0-9_-]*$", name)) and 2 < len(name) < 15 else False
    else:
        return False
