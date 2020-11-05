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
JSON_FILE_TYPE = '.json'
TEXT_FILE_TYPE = '.txt'
AUDIO_FILE_TYPE = '.mp3'
VIDEO_FILE_TYPE = '.mp4'


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
    file_type = {
        'text': TEXT_FILE_TYPE,
        'audio': AUDIO_FILE_TYPE,
        'video': VIDEO_FILE_TYPE
    }

    def get(self, request, format=None):
        historias = Historia.objects.all()
        serializer = HistoriaSerializer(historias, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def post(self, request, format=None):
        try:
            data = request.data

            info_filename = data['title'] + JSON_FILE_TYPE
            media_filename = data['title'] + self.file_type[data['type']]
            s3_folder_path = BASE_PATH + data['title'] + '/'

            historia = Historia.objects.create(
                title=data["title"],
                description=data["description"],
                type=data["type"],
                # media=data["media"]
            )

            serializer = HistoriaSerializer(historia)
            self.upload_to_s3(data, s3_folder_path, info_filename, media_filename, serializer)

            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        except Exception as e:
            raise e

    def upload_to_s3(self, data, s3_folder_path, info_filename, media_filename, serializer):
        s3object = _S3.Object(AWS_STORAGE_BUCKET_NAME, s3_folder_path + info_filename)
        s3object.put(
            Body=(JSONRenderer().render(serializer.data))
        )
        s3object_media = _S3_client.upload_fileobj(data['media'], AWS_STORAGE_BUCKET_NAME,
                                                   s3_folder_path + media_filename)
