from django.contrib import admin
from django.urls import path, include
from backend_api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BookView.as_view(), name='oh_shit'),
    path('', SaveContactMessageView.as_view(), name='save_contact_message'),
]

