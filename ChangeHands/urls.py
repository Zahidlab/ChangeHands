
from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('register/', views.register, name = 'register'),
    path('home', views.home, name = 'home'),
    path('login', views.login, name = 'login'),
]
