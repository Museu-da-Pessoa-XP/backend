
from django.db import models

USER_MAX_LENGTH = 30


class User(models.Model):
    name = models.CharField(max_length=USER_MAX_LENGTH)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=15)


class Tag(models.Model):
    tag = models.CharField(
        max_length=24,
        default=''
    )


class Historia(models.Model):
    title = models.CharField(
        max_length=140,
        default='Um lindo título'
    )
    type = models.CharField(
        max_length=5,
        default='text'
    )
    media_url = models.CharField(
        max_length=2048,
        default=''
    )
    tags = models.ManyToManyField(Tag)


