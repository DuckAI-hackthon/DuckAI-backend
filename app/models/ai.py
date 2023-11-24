from django.db import models

class Ai(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name