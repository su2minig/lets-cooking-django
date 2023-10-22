from django.urls import path
from . import views

urlpatterns = [
    path('', views.save, name='save'),
    path('<int:pk>/', views.recipedetail, name='recipedetail'),
]