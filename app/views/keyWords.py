from rest_framework.viewsets import ModelViewSet

from app.models import KeyWords
from app.serializers import KeyWordsSerializer

class KeyWordsViewSet(ModelViewSet):
    queryset = KeyWords.objects.all()
    serializer_class = KeyWordsSerializer
