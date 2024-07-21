from django.db import models

# Create your models here.

class Library(models.Model):
    book = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    
    