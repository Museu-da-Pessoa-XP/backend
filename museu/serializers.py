
from rest_framework import serializers

from .models import User, Historia


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'id']


class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = ['title', 'description', 'type']

