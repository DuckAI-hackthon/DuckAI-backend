from rest_framework.serializers import ModelSerializer

from app.models import Historic

class HistoricSerializer(ModelSerializer):
    class Meta:
        model = Historic
        fields = "__all__"