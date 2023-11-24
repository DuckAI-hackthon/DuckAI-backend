from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
import json
from src.gpt import qea, translate, summarize, get_keywords, summarize_in
from app.models import Historic, Ai
from usuario.models import Usuario

from django.shortcuts import get_object_or_404


@api_view(["GET"])
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

    if ai == 1:
        if type == 1:
            response = qea(text)
            print(response)
        elif type == 2:
            response = translate(text, from_lang, to_lang)
            print(response)
        elif type == 3:
            response = summarize(text, amount)
            print(response)
        elif type == 4:
            response = get_keywords(text, keyNum)
            print(response)
        elif type == 5:
            response = summarize_in(text, words)
            print(response)

    elif ai == 2:
        print("gpt-3.5")

    user_instance = get_object_or_404(Usuario, id=user_id)
    ai_instance = get_object_or_404(Ai, id=ai)

    Historic.objects.create(ai=ai, type=type, question=text, user=user_instance, choice=response)
    
    return Response({"ai": ai, "type": type, "text": text, "user_id": user_id, "response": response})