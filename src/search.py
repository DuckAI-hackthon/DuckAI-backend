from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
import json
from src.gpt import qeaGPT, translateGPT, summarizeGPT, get_keywordsGPT, summarize_inGPT
from src.llama import qeaLlama, translateLlama, summarizeLlama, get_keywordsLlama, summarize_inLlama
from src.hercai import qeaHercai, translateHercai, summarizeHercai, get_keywordsHercai
from app.models import Historic, Ai, Function, ChatHistory, Chat
from usuario.models import Usuario

from django.shortcuts import get_object_or_404


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def search(request):
    ai = int(request.GET.get("ai"))
    type = int(request.GET.get("type"))
    data = json.loads(request.body.decode('utf-8'))

    text = data.get('text', '')
    user_id = int(data.get('user_id', ''))

    from_lang = data.get('from_lang', '')
    to_lang = data.get('to_lang', '')

    amount = data.get('amount', '')

    keyNum = data.get('keyNum', '')

    words = data.get('words', '')

    # Inicialize a variável response com um valor padrão
    response = None
    print(type, ai)

    user_instance = get_object_or_404(Usuario, id=user_id)
    ai_instance = get_object_or_404(Ai, id=ai)
    type_instance = get_object_or_404(Function, id=type)

    chat = Chat.objects.filter(user=user_instance)
    if ai == 1:
        if type == 1:
            response = qeaGPT(text)
            chatHistory = ChatHistory.objects.create(ai=ai_instance, function=type_instance, question=text, choice=response)
            chatHistory.chat.set(chat)
            chatHistory.save()
            print(response)
        elif type == 2:
            response = translateGPT(text, from_lang, to_lang)
            print(response)
        elif type == 3:
            response = summarize_inGPT(text,"100")
            print(response)
        elif type == 4:
            response = get_keywordsGPT(text, keyNum)
            print(response)
    elif ai == 2:
        if type == 1:
            response = qeaLlama(text)
            chatHistory = ChatHistory.objects.create(ai=ai_instance, function=type_instance, question=text, choice=response)
            chatHistory.chat.set(chat)
            chatHistory.save()
            print(response)
        elif type == 2:
            response = translateLlama(text, from_lang, to_lang)
            print(response)
        elif type == 3:
            if amount != '':
                response = summarizeLlama(text, amount)
            elif words != '':
                response = summarize_inLlama(text, words)
            print(response)
        elif type == 4:
            response = get_keywordsLlama(text, keyNum)
            print(response)

    elif ai == 3:
        if type == 1:
            response = qeaHercai(text)
            chatHistory = ChatHistory.objects.create(ai=ai_instance, function=type_instance, question=text, choice=response)
            chatHistory.chat.set(chat)
            chatHistory.save()
            print(response)
        elif type == 2:
            response = translateHercai(text, from_lang, to_lang)
            print(response)
        elif type == 3:
            response = summarizeHercai(text)
            print(response)
        elif type == 4:
            response = get_keywordsHercai(text, keyNum)
            print(response)

    Historic.objects.create(ai=ai_instance, function=type_instance, question=text, user=user_instance, choice=response)
    
    return Response({"ai": ai, "type": type, "text": text, "user_id": user_id, "response": response})