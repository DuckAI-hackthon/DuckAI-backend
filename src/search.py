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
def search(request):
    ai = request.GET.get("ai")
    type = request.GET.get("type")
    data = json.loads(request.body.decode('utf-8'))

    text = data.get('text', '')
    user_id = data.get('user_id', '')

    print(ai, type, text, user_id)

    return Response({"ai": ai, "type": type, "text": text, "user_id": user_id})