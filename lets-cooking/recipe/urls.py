from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe, name='recipe'),
    path('<int:pk>/', views.recipedetail, name='recipedetail'),
]