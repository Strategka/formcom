import re
from datetime import datetime


def make_guess_type(*is_types):
    def guess_type(val):
        for is_type in is_types:
            if type := is_type(val):
                break
        return type
    return guess_type


def is_date(val):
    for f in ['%d.%m.%Y', '%Y-%m-%d']:
        try:
            datetime.strptime(val, f)
            return "date"
        except ValueError:
            pass

def is_phone(val):
    return "phone" if re.fullmatch(r"\+7 [0-9]{3} [0-9]{3} [0-9]{2} [0-9]{2}", val) else None

def is_email(val):
    return "email" if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", val) else None

def is_text(val):
    return 'text'
