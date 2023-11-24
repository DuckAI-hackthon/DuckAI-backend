from rest_framework.viewsets import ModelViewSet

from app.models import Translation
from app.serializers import TranslationSerializer

class TranslationViewSet(ModelViewSet):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer