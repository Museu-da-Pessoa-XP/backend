from rest_framework import viewsets
from rest_framework import permissions

from museubackend.upload.models import Upload
from museubackend.museubackend.storage import LocalStorage


class UploadViewSet(viewsets.ModelViewSet):
    queryset = Upload.uploaded_at
    serializer_class = None
    permission_classes = [permissions.IsAuthenticated]

    fs = LocalStorage()
    filename = fs.save(image_file.name, image_file)
    image_url = fs.url(filename)