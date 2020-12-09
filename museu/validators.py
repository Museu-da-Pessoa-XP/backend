
from django.core.exceptions import ValidationError

ALLOWED_TYPES = ['audio', 'text', 'video']


def validate_historia_type(value):
    """
    Validates the Historia types
    """
    if value not in ALLOWED_TYPES:
        raise ValidationError('%s is not an valid Historia type'
                              % value, params={'value': value})
