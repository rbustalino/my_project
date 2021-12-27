from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('application/',include('application.urls')),
    path('admin/', admin.site.urls),
    
]