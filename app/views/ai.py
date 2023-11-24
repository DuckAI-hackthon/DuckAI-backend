from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
import json

@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def ai(request):
    ai = request.GET.get("ai")
    type = request.GET.get("type")
    data = json.loads(request.body.decode('utf-8'))

            # Acesse o valor associado à chave "text"
    text = data.get('text', '')

    print(ai, type, text)

    return Response({"ai": ai, "type": type, "text": text}, )