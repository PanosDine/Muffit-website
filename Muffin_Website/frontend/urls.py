from django.urls import path
from .views import index #contact

urlpatterns = [
    path('', index),
    path('about', index),
    path('contact', index),
    path('order', index),
]