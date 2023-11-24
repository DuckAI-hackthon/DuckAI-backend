from django.db import models
from django.utils import timezone

from .ai import Ai
from .function import Function
from .chat import Chat

class ChatHistory(models.Model):
    chat = models.ManyToManyField(Chat, related_name='chat_history', default=None)
    question = models.CharField(max_length=200, default=None)
    choice = models.CharField(max_length=200, default=None)
    date = models.DateTimeField('date published', default=timezone.now, blank=True, null=True)
    ai = models.ForeignKey(Ai, on_delete=models.CASCADE, default=None)
    function = models.ForeignKey(Function, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.question