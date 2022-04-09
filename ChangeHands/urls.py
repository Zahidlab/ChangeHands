
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
    path('profile/<int:sid>', views.profile, name = 'profile'),
    path('add_product', views.add_product, name = 'add_product'),
    path('view_product/<int:id>', views.view_product, name = 'view_product'),
    path('comment', views.comment, name = 'comment'),
    path('seller/<int:sid>', views.seller, name = 'seller'),
    path('edit_product/<int:id>', views.edit_product, name = 'edit_product'),
    path('edit_profile/<int:sid>', views.edit_profile, name = 'edit_profile'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
