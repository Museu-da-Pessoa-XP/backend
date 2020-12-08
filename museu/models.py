
from django.db import models

from museu.validators import validate_historia_type

USER_MAX_LENGTH = 30


class User(models.Model):
    name = models.CharField(max_length=USER_MAX_LENGTH)
    email = models.EmailField(max_length=254)


class Historia(models.Model):
    title = models.CharField(
        max_length=140,
        default='Um lindo título'
    )
    description = models.CharField(
        max_length=280,
        default='Uma bela descrição'
    )
    type = models.CharField(
        max_length=5,
        default='text',
        validators=[validate_historia_type]
    )
    media_url = models.CharField(
        max_length=2048,
        default=''
    )
