from rest_framework.serializers import ModelSerializer

from app.models import Favorite

class FavoriteSerializer(ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"