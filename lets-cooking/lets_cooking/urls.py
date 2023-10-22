from django.urls import path
from . import views

urlpatterns = [
    path('', views.lets_cooking, name='lets_cooking'),
]