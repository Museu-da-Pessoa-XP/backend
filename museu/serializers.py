from rest_framework import serializers
from .models import User, Historia, Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone']


class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = ['user', 'title', 'type', 'media_url', 'tags']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag']
