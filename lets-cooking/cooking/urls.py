# tutorialdjango > urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lets_cooking/', include('lets_cooking.urls')),
    path('recipe/', include('recipe.urls')),
    path('save/', include('save.urls')),
]