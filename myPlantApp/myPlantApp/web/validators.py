from django.core.exceptions import ValidationError


def start_with_capital_letter(value):
    if value[0].isupper():
        return value
    raise ValidationError("Your name must start with a capital letter!")
