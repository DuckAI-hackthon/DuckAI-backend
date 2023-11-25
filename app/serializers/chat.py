from rest_framework.serializers import ModelSerializer

from app.models import Chat

class ChatSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"