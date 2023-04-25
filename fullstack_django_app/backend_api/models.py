from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    link = models.CharField(max_length =2000, null=True, blank=True)
    cost = models.CharField(max_length =100, null=True, blank=True)