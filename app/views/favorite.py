from rest_framework.viewsets import ModelViewSet

from app.models import Favorite
from app.serializers import FavoriteSerializer

class FavoriteViewSet(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
