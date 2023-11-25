from rest_framework.serializers import ModelSerializer

from app.models import Ai

class AiSerializer(ModelSerializer):
    class Meta:
        model = Ai
        fields = "__all__"
        depth = 1