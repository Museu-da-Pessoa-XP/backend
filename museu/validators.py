from django.core.exceptions import ValidationError

ALLOWED_TYPES = ['audio', 'text', 'video']


def validate_historia_type(value):
    if value not in ALLOWED_TYPES:
        raise ValidationError(f'{value} is not an valid Historia type', params={'value': value})
