from rest_framework.viewsets import ModelViewSet

from app.models import Ai
from app.serializers import AiSerializer

class AiViewSet(ModelViewSet):
    queryset = Ai.objects.all()
    serializer_class = AiSerializer
