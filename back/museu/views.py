from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import User, Historia, Upload
from .serializers import UserSerializer, HistoriaSerializer, UploadSerializer
import json

class UserView(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe = False)

    def post(self, request, format=None):
        try:
            dados = json.loads(request.data['data'])
            user = User.objects.create(
                nome = dados[0]["nome"],
                email = dados[0]["email"],
            )
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse("", safe=False)

class HistoriaView(APIView):
    def get(self, request, format=None):
        historias = Historia.objects.all()
        serializer = HistoriaSerializer(historias, many=True)
        return JsonResponse(serializer.data, safe = False)

    def post(self, request, format=None):
        try:
            dados = json.loads(request.data['data'])
            user = User.objects.get(nome=dados[0]["usuario"])
            historia = Historia.objects.create(
                nome = dados[0]["nome"],
                localizacao = dados[0]["localizacao"],
                usuario = user,
            )
            serializer = HistoriaSerializer(historia)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse("", safe=False)

class UploadView(APIView):
    def get(self, request, format=None):
        uploads = Upload.objects.all()
        serializer = UploadSerializer(uploads, many=True)
        return JsonResponse(serializer.data, safe = False)

    def post(self, request, format=None):
        try:
            dados = json.loads(request.data['data'])
            upload = Upload.objects.create(
                uploaded_at=dados[0]["uploaded_at"],
                file=dados[0]["file"],
            )
            serializer = UploadSerializer(upload)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse("", safe = False)