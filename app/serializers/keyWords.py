from rest_framework.serializers import ModelSerializer

from app.models import KeyWords

class KeyWordsSerializer(ModelSerializer):
    class Meta:
        model = KeyWords
        fields = "__all__"