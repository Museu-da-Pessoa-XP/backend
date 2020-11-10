import json

from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from museu.models import User, Historia
from museu.serializers import UserSerializer, HistoriaSerializer


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
            historia = Historia.objects.create(
                title=data["title"],
                description=data["description"],
                type=data["type"]
            )
            serializer = HistoriaSerializer(historia)
            return JsonResponse(data, status=status.HTTP_201_CREATED, safe=False)
        except Exception as e:
            raise e
