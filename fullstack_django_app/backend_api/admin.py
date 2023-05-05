from django.contrib import admin

# Register your models here.
from .models import Book, ContactMessage, UserLogin

admin.site.register(Book)
admin.site.register(ContactMessage)
admin.site.register(UserLogin)