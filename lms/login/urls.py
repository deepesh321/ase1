"""lms URL Configuration

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
    2. Add a UruRL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_display,name='login'),
    path('register/', views.register_display,name='register'),
    path('hom/',views.home_display,name='out_home'),
    path('home/',views.inhome_display,name='in_home'),
    path('register/otp_verify/',views.otp_verify,name='otp'),
    path('home/logout/',views.logout_view,name='logout'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('reset_password/',views.reset_password,'reset'),
    path('reset_password/reset_otp_verify/',views.reset_password,name='login'),
    path('reset_password/reset_otp_verify/save_password/',views.save_password,name='save_password')
    ]