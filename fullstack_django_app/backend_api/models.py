from django.db import models

# Create your models here.
class Book(models.Model):
    # Place for creating models 
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    link = models.CharField(max_length =2000, null=True, blank=True)
    cost = models.CharField(max_length =100, null=True, blank=True)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
# models.py

class UserLogin(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True, default="")
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)