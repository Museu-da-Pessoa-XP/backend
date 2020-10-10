from django.db import models

from museubackend.museubackend.storage import LocalStorage


class Upload(models.Model):
    uploaded_at = models.DateTimeField()
    file = models.FileField(storage=LocalStorage())
