# abcpHome/urls.py

from django.urls import path
from django.contrib import admin  # Import the admin module
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login-register/', views.login_register, name='login_register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Using Django's built-in logout view
    path('potb/', views.potb, name='potb'),
    path('tech-dot/<int:pk>/', views.tech_dot_detail, name='tech_dot_detail'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),  # Separate pattern for editing profile
    path('profile/<str:username>/', views.profile, name='profile'),
    path('news-feed/', views.news_feed, name='news_feed'),
    path('add-my-prayer/', views.add_my_prayer, name='add_my_prayer'),
    path('add-prayer-intercession/', views.add_prayer_intercession, name='add_prayer_intercession'),
    path('signup/', views.signup, name='signup'),  # Added signup URL pattern
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
]
