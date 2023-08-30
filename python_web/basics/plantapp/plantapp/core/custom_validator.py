from django.core.exceptions import ValidationError


def starts_capital_letter(name):
    msg = "Your name must start with a capital letter!"
    if not name[0].isupper():
        raise ValidationError(msg)

def contains_only_letters(name):
    msg = "Plant name should contain only letters!"
    if not all([letter.isalpha() for letter in name]):
        raise ValidationError(msg)