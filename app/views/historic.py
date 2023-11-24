from rest_framework.viewsets import ModelViewSet

from app.models import Historic
from app.serializers import HistoricSerializer

class HistoricViewSet(ModelViewSet):
    queryset = Historic.objects.all()
    serializer_class = HistoricSerializer
