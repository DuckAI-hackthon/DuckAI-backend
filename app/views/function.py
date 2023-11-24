from rest_framework.viewsets import ModelViewSet

from app.models import Function
from app.serializers import FunctionSerializer

class FunctionViewSet(ModelViewSet):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer
