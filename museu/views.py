from rest_framework import status
from rest_framework.views import APIView
from django.http.response import JsonResponse
from museu.models import User, Historia
from museu.serializers import UserSerializer, HistoriaSerializer
import json


class UserView(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        try:
            data = json.loads(request.data['data'])
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
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        try:
            data = json.loads(request.data['data'])
            user = User.objects.get(id=data["user_id"])
            historia = Historia.objects.create(
                name=data["name"],
                location=data["location"],
                user=user,
            )
            serializer = HistoriaSerializer(historia)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        except Exception as e:
            raise e
