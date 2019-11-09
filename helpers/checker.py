import re


def is_valid_email(email):
    return True if re.search(r'[a-z]@[a-z].', email) else False
    # return True if re.search(r'[a-zA-Z0-9]@[a-z][.][a-z]', email) else False


def is_valid_password(password):
    '''
        можешь усложнить как нибудь, а то валидация выглядит как будто для галочки
    :param password:
    :return:
    '''
    upper_case = 0
    lower_case = 0
    number = 0
    for char in password:
        if char.isupper():
            upper_case += 1
        if char.islower():
            lower_case += 1
        if char.isdigit():
            number += 1
    return True if 5 < len(password) < 15 and upper_case and lower_case and number else False


def is_valid_age(age):
    return True if 15 < age < 100 else False


def is_valid_name(name):
    if isinstance(name, str):
        return True if name.isalpha() and 2 < len(name) < 15 else False
    else:
        return False
