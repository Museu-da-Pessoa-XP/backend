import json
import hashlib

import boto3
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

from backend.settings import AWS_STORAGE_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from museu.models import User, Historia
from museu.serializers import UserSerializer, HistoriaSerializer

_S3 = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                     aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
_S3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
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

    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, format=None):
        historias = Historia.objects.all()
        serializer = HistoriaSerializer(historias, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def post(self, request, format=None):
        try:

            data = {
                'title': request.data['title'],
                'description': request.data['description'],
                'type': request.data['type'],
                'media': request.data['media']
            }

            file_type = data['title'] + '.json'
            media_type = 'video.mp4'

            path = BASE_PATH + data['title'] + '/'

            historia = Historia.objects.create(
                title=data["title"],
                description=data["description"],
                type=data["type"],
                # media=data["media"]
            )

            serializer = HistoriaSerializer(historia)
            s3object = _S3.Object(AWS_STORAGE_BUCKET_NAME, path+file_type)
            s3object.put(
                Body=(JSONRenderer().render(serializer.data))
            )
            s3object_media = _S3_client.upload_fileobj(data['media'], AWS_STORAGE_BUCKET_NAME, path+media_type)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        except Exception as e:
            print(e)
            raise e
