from django.db import models

# Create your models here.

class Orders(models.Model):
  title = models.CharField(max_length=150)
  foods = models.CharField(max_length=150)