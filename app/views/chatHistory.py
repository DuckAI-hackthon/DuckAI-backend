from rest_framework.viewsets import ModelViewSet

from app.models import ChatHistory
from app.serializers import ChatHistorySerializer

class ChatHistoryViewSet(ModelViewSet):
    queryset = ChatHistory.objects.all()
    serializer_class = ChatHistorySerializer
