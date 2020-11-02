import json
import hashlib

import boto3
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

from backend.settings import AWS_STORAGE_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from museu.models import User, Historia
from museu.serializers import UserSerializer, HistoriaSerializer

_S3 = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                     aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
BASE_PATH = 'uploads/'


class UserView(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def post(self, request, format=None):
        try:
            data = json.loads(request.body)['data']
            user = User.objects.create(
                name=data["name"],
                email=data["email"],
            )
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        except Exception as e:
            raise e


class HistoriaView(APIView):

    def get(self, request, format=None):
        historias = Historia.objects.all()
        serializer = HistoriaSerializer(historias, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def post(self, request, format=None):
        try:
            data = json.loads(request.body)
            data_string = json.dumps(data).encode('UTF-8')
            data_hash = hashlib.md5(data_string).hexdigest()
            file_type = '.json'
            path = BASE_PATH + str(data_hash) + file_type

            historia = Historia.objects.create(
                title=data["title"],
                description=data["description"],
                type=data["type"]
            )

            serializer = HistoriaSerializer(historia)

            s3object = _S3.Object(AWS_STORAGE_BUCKET_NAME, path)
            s3object.put(
                Body=(JSONRenderer().render(serializer.data))
            )
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        except Exception as e:
            raise e
