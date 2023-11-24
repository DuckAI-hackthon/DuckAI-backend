from rest_framework.viewsets import ModelViewSet

from app.models import Resume
from app.serializers import ResumeSerializer

class ResumeViewSet(ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer