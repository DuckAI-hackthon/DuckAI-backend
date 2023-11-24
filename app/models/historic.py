from django.db import models 
from django.utils import timezone

from usuario.models import Usuario
from .ai import Ai
from .function import Function

class Historic(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    choice = models.CharField(max_length=200)
    date = models.DateTimeField('date published', default=timezone.now, blank=True, null=True)
    ai = models.ForeignKey(Ai, on_delete=models.CASCADE)
    function = models.ForeignKey(Function, on_delete=models.CASCADE)