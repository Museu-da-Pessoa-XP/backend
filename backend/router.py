from museu.viewsets import AppViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('historia', AppViewSet)
