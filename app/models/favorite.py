from django.db import models

from usuario.models import Usuario
from .historic import Historic

class Favorite(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    historic = models.ForeignKey(Historic, on_delete=models.CASCADE)