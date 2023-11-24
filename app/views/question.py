from rest_framework.viewsets import ModelViewSet

from app.models import Question
from app.serializers import QuestionSerializer

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer