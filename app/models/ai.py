from django.db import models
from uploader.models import Image
class Ai(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    image = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.name