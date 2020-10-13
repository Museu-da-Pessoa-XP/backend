from django.db import models

from museu.storage import LocalStorage


class User(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

class Historia(models.Model):
    nome = models.CharField(max_length=30)
    localizacao = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)

class Upload(models.Model):
    uploaded_at = models.DateTimeField()
    file = models.FileField(storage=LocalStorage())