from museu.viewsets import UserViewset, HistoriaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', UserViewset)
router.register('historia', HistoriaViewset)


