from rest_framework.viewsets import ModelViewSet

from app.models import Chat
from app.serializers import ChatSerializer

class ChatViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
