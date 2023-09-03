from unicodedata import name
from django.db import models

# Create your models here.
class db(models.Model):
    name=models.CharField(max_length=50)
    feed=models.TextField(max_length=50)