from museu.viewsets import HistoriaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('historia', HistoriaViewset)


