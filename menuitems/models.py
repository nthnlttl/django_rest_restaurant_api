from django.db import models

# Create your models here.

class Menuitems(models.Model):
    DRINKS = "Drinks"
    APPETIZERS = "Appetizers"
    ENTREES = "Entrees"
    
    CATEGORY_CHOICES = [
        (DRINKS, 'Drinks'),
        (APPETIZERS, 'Appetizers'),
        (ENTREES, 'Entrees'),
    ]

    category = models.CharField(
        null=True,
        choices=CATEGORY_CHOICES,
        default=ENTREES,
        max_length=30,
    )
    
    
    
    
    name = models.CharField(max_length=255)
    cost = models.PositiveIntegerField(null=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name