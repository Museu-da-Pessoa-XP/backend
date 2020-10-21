from django.db import models

USER_MAX_LENGTH = 30


class User(models.Model):
    name = models.CharField(max_length=USER_MAX_LENGTH)
    email = models.EmailField(max_length=254)


class Historia(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=255)
    user = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)
