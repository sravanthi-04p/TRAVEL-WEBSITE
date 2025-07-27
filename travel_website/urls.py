from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # Admin route
    path('', include('main.urls')),          # Link to app-level `urls.py`
]
