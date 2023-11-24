from rest_framework.serializers import ModelSerializer

from app.models import ChatHistory

class ChatHistorySerializer(ModelSerializer):
    class Meta:
        model = ChatHistory
        fields = "__all__"