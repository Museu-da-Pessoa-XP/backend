from rest_framework import viewsets
from . import models
from . import serializers


class AppViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.HistoriaSerializer
