from rest_framework.viewsets import ModelViewSet

from app.models import ChatHistory
from app.serializers import ChatHistorySerializer

class ChatHistoryViewSet(ModelViewSet):
    queryset = ChatHistory.objects.all()
    serializer_class = ChatHistorySerializer

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from app.models import Ai, Chat
from usuario.models import Usuario
from django.shortcuts import get_object_or_404

@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def getChatHistoricUser(request):
    user_id = request.GET.get('user_id')
    ai_id = int(request.GET.get('ai_id'))

    # Obtém as instâncias de usuário e AI
    user_instance = get_object_or_404(Usuario, id=user_id)
    chat_instance = get_object_or_404(Chat, user=user_instance)
    print(ai_id)
    ai_instance = Ai.objects.get(name="GPT")
    if ai_id == 1:
        print('aqui')
        ai_instance = Ai.objects.get(name="GPT")
    elif ai_id == 2:
        ai_instance = Ai.objects.get(name="Llama")
    elif ai_id == 3:
        ai_instance = Ai.objects.get(name="Hercai")

    print(ai_instance)
    # Filtra os históricos de bate-papo com base nas instâncias de usuário e AI
    chat_histories = ChatHistory.objects.filter(chat=chat_instance, ai=ai_instance)

    serializer = ChatHistorySerializer(chat_histories, many=True)

    return Response({"response": serializer.data})
