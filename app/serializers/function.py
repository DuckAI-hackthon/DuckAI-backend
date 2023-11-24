from rest_framework.serializers import ModelSerializer

from app.models import Function

class FunctionSerializer(ModelSerializer):
    class Meta:
        model = Function
        fields = "__all__"