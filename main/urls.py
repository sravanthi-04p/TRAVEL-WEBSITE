from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Main homepage
    path('', views.home, name='home'),  # Route for the homepage

    # Search functionality
    path('search/', views.search, name='search'),

    # Authentication routes
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
]
