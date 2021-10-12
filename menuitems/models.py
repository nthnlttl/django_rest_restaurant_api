from django.db import models

# Create your models here.

class Menu(models.Model):
    item: models.CharField(max_length=255)
    cost: models.CharField(max_length=255)
    description: models.CharField(max_length=255)
