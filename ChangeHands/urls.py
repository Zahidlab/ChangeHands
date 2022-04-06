
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('register/', views.register, name = 'register'),
    path('home', views.home, name = 'home'),
    path('login', views.loginpage, name = 'login'),
    path('logout', views.logoutpage, name = 'logout'),
    path('profile', views.profile, name = 'profile'),
    path('add_product', views.add_product, name = 'add_product'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
