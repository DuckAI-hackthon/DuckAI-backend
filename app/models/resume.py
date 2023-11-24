from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from usuario.models import Usuario

class Resume(models.Model): 
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    date = models.DateTimeField('date published', default=timezone.now, blank=True, null=True)

