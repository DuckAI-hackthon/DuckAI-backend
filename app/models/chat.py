from django.db import models

from usuario.models import Usuario

class Chat(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)