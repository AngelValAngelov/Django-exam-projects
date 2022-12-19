from django.core.exceptions import ValidationError


def validate_only_letters(value):
    if not all(ch.isalpha() or ch.isnumber() or ch == '_' for ch in value):
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')
