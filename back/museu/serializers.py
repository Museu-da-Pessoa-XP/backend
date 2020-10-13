from rest_framework import serializers
from museu.models import User, Historia, Upload

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nome', 'email']

class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = ['nome', 'localizacao', 'usuario']

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ['uploaded_at', 'file']

