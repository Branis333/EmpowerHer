"""
URL configuration for django_project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('register/', user_views.register, name='register'),  # Registration page
    path('profile/', user_views.profile, name='profile'),  # Profile page
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),  # Logout page
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),  # Password reset request
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),  # Confirmation that reset email was sent
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),  # Reset password link
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),  # Password reset completion
    path('', include('blog.urls')),  # Blog URLs (root)
]
