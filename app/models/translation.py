from django.db import models

class Translation(models.Model): 
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    date = models.DateTimeField('date published')