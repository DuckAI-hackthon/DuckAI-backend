from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from app.models import Translation
from app.serializers import TranslationSerializer

class TranslationViewSet(ModelViewSet):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    permission_classes = [IsAuthenticated]