from django.db import models

# Create your models here.
class Hero(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    char_class = models.CharField(max_length=255)