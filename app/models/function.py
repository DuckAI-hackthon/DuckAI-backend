from django.db import models
from uploader.models import Image
class Function(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    icon = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.name