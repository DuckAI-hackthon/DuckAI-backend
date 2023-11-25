from rest_framework.viewsets import ModelViewSet

from app.models import Historic
from app.serializers import HistoricSerializer

class HistoricViewSet(ModelViewSet):
    queryset = Historic.objects.all()
    serializer_class = HistoricSerializer

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response

@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def get_historic_by_user(request):
    user_id = int(request.GET.get("user_id"))

    historic = Historic.objects.filter(user=user_id)

    return Response({"historic": historic})