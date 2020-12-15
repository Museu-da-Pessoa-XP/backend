from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

from backend.settings import AWS_STORAGE_BUCKET_NAME
from museu.models import User, Historia, Tag
from museu.serializers import HistoriaSerializer

import boto3

_S3 = boto3.resource('s3')
_S3_client = boto3.client('s3')

BASE_PATH = 'uploads/'


class AppView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    # TODO: Missing return User
    def get(self, request):
        historias = Historia.objects.all()
        hist_data = HistoriaSerializer(historias, many=True).data
        return JsonResponse(hist_data, status=status.HTTP_200_OK, safe=False)

    def post(self, request):
        try:
            data = request.data
            media_filename_extension = data['media'].content_type.split('/')[1]
            if len(media_filename_extension) <= 1:
                status_error = status.HTTP_500_INTERNAL_SERVER_ERROR
                return JsonResponse('file is empty',
                                    status=status_error,
                                    safe=False)

            media_filename = data['title'] + '.' + media_filename_extension
            s3_folder_path = BASE_PATH + data['title'] + '/'

            status_code = self.upload_to_s3(data,
                                            s3_folder_path,
                                            media_filename)

            if not status.is_success(status_code):
                status_error = status.HTTP_500_INTERNAL_SERVER_ERROR
                return JsonResponse('error',
                                    status=status_error,
                                    safe=False)

            tag_objs = self.save_tags(data['tags'])
            user = self.save_user(data['name'], data['email'], data['phone'])
            historia = self.save_historia(user, data['title'], data['type'],
                                          s3_folder_path + media_filename,
                                          tag_objs)

            serializer = HistoriaSerializer(historia)
            return JsonResponse(serializer.data,
                                status=status_code,
                                safe=False)

        except Exception as error:
            raise error

    def upload_to_s3(self, data, s3_folder_path, media_filename):
        s3object = _S3.Object(AWS_STORAGE_BUCKET_NAME,
                              s3_folder_path + media_filename)
        put_metadata = s3object.put(Body=(data['media']))
        response_code = put_metadata['ResponseMetadata']['HTTPStatusCode']
        return response_code

    def save_tags(self, tags):
        tag_objs = []
        for tag in tags.split(','):
            tag_obj = Tag.objects.create(tag=tag)
            tag_obj.save()
            tag_objs.append(tag_obj)
        return tag_objs

    def save_historia(self, user, title, historia_type, media_url, tags):
        historia = Historia.objects.create(
            user=user,
            title=title,
            type=historia_type,
            media_url=media_url,
        )
        historia.save()
        for tag in tags:
            historia.tags.add(tag)
        return historia

    def save_user(self, name, email, phone):
        phone = "".join([c if c.isdigit() else '' for c in phone])

        user = User.objects.create(
            name=name,
            email=email,
            phone=phone
        )
        user.save()
        return user
