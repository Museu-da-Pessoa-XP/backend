import boto3
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

from backend.settings import AWS_STORAGE_BUCKET_NAME
from museu.models import User, Historia, Tag
from museu.serializers import HistoriaSerializer

_S3 = boto3.resource('s3')
_S3_client = boto3.client('s3')

BASE_PATH = 'uploads/'


class AppView(APIView):
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

            tag_objs = self.save_tags(data['tags'])
            historia = self.save_historia(data['title'], data['type'], s3_folder_path + media_filename, tag_objs)
            self.save_user(data['name'].data['email'], data['telephone'])

            serializer = HistoriaSerializer(historia)
            return JsonResponse(serializer.data, status=status_code, safe=False)

        except Exception as e:
            raise e

    def upload_to_s3(self, data, s3_folder_path, media_filename):
        s3object = _S3.Object(AWS_STORAGE_BUCKET_NAME, s3_folder_path + media_filename)
        put_metadata = s3object.put(Body=(data['media']))
        response_code = put_metadata['ResponseMetadata']['HTTPStatusCode']
        return response_code

    def save_tags(self, tags):
        tag_objs = []
        for tag in tags:
            tag_obj = Tag.objects.create(tag=tag)
            tag_obj.save()
            tag_objs.append(tag_obj)
        return tag_objs

    def save_historia(self, title, historia_type, media_url, tags):
        historia = Historia.objects.create(
            title=title,
            type=historia_type,
            media_url=media_url
        )
        historia.save()
        for tag in tags:
            historia.tags.add(tag)
        return historia

    def save_user(self, name, email, telephone):
        telephone = "".join([c if c.isdigit() else '' for c in telephone])

        user = User.objects.create(
            name=name,
            email=email,
            telephone=telephone
        )
        user.save()
