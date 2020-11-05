import json
import boto3
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

from backend.settings import AWS_STORAGE_BUCKET_NAME
from museu.models import User, Historia
from museu.serializers import UserSerializer, HistoriaSerializer

_S3 = boto3.resource('s3')
_S3_client = boto3.client('s3')

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

    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, format=None):
        historias = Historia.objects.all()
        serializer = HistoriaSerializer(historias, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def post(self, request, format=None):
        try:
            data = request.data
            media_filename_extension = data['media'].content_type.split('/')[1]
            if len(media_filename_extension) <= 1:
                return JsonResponse('file is empty', status=status.HTTP_500_INTERNAL_SERVER_ERROR, safe=False)

            media_filename = data['title'] + '.' + media_filename_extension
            s3_folder_path = BASE_PATH + data['title'] + '/'
            status_code = self.upload_to_s3(data, s3_folder_path, media_filename)
            if not status.is_success(status_code):
                return JsonResponse('error', status=status.HTTP_500_INTERNAL_SERVER_ERROR, safe=False)

            historia = Historia.objects.create(
                title=data["title"],
                description=data["description"],
                type=data["type"],
                media_url=s3_folder_path + media_filename
            )

            serializer = HistoriaSerializer(historia)
            return JsonResponse(serializer.data, status=status_code, safe=False)

        except Exception as e:
            print(e)
            raise e

    def upload_to_s3(self, data, s3_folder_path, media_filename):
        s3object = _S3.Object(AWS_STORAGE_BUCKET_NAME, s3_folder_path + media_filename)
        put_metadata = s3object.put(Body=(data['media']))
        response_code = put_metadata['ResponseMetadata']['HTTPStatusCode']
        return response_code
