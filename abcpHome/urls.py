# abcpHome/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login-register/', views.login_register, name='login_register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('potb/', views.potb, name='potb'),
    path('tech-dot/<int:pk>/', views.tech_dot_detail, name='tech_dot_detail'),
]
