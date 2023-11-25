from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import AllowAny
from usuario.models import Usuario
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate, get_user_model
import json
User = get_user_model()

@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny]) 
def create_user(request):
        email = request.data.get("email")
        password = request.data.get("password")
        name = request.data.get("name")
        birth = request.data.get("birth")

        if Usuario.objects.filter(email=email).exists():
            return Response({"error": "Email já cadastrado"}, status=400)
        if email and password:
              user = Usuario.objects.create(email=email)  
              user.set_password(password)
              user.name = name
              user.birth = birth
              user.save()
              return Response({"message": "Usuário cadastrado com sucesso."}, status=201)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny]) 
def get_user(request):
    data = json.loads(request.body.decode('utf-8'))
    email = data.get("email", '')
    password = data.get("password", '')
    print(email, password)

    if email is not None and password is not None:
        try:
            user = User.objects.get(email=email)
            name = user.name
            print(name)
            user = authenticate(email=email, password=password)
        except User.DoesNotExist:
            user = None
            
    else:
        return Response(
            {"message": "Credenciais inválidas!"}, status=status.HTTP_400_BAD_REQUEST
        )

    print(user)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        access = AccessToken.for_user(user)

        response_data = {
            "refresh": str(refresh),
            "access": str(access),
            "username": user.name,
            "email": user.email,
            "id": user.id,
            "message": "Login realizado com sucesso!"
            # Adicione outros campos do usuário que você deseja retornar
        }
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        return Response(
            {"message": "Credenciais inválidas!"}, status=status.HTTP_400_BAD_REQUEST
        )
