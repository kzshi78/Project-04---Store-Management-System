import re


def is_valid_phone(phone):

    pattern = r"^09\d{9}$"

    result = re.search(pattern, phone)

    if result:
        return True

    return False