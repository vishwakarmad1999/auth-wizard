"""user_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.contrib.auth.views import (
                                        LoginView, 
                                        LogoutView,
                                        PasswordResetView,
                                        PasswordResetDoneView,
                                        PasswordResetConfirmView,
                                        PasswordResetCompleteView,
                                        )
from profiles.views import UserCreate, HomeView, verify_activation_key, register_confirm

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', HomeView.as_view(), name = 'home'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('pass-reset/', PasswordResetView.as_view(), name = 'password_reset'),
    path('pass-reset-sent', PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('pass-reset-confirm/(<slug:uidb64>)-(<slug:token>)/', PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'), 
    path('pass-reset-final', PasswordResetCompleteView.as_view(), name = 'password_reset_complete'), 
    path('register/', UserCreate.as_view(), name = 'register'),
    path('register-confirm/', register_confirm, name = 'register_confirm'),
    path('<str:key>/', verify_activation_key, name = 'verify'),
]
