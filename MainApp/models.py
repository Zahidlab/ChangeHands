# from datetime import timezone
from pickle import TRUE

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.db.models.fields import AutoField, CharField, IntegerField
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        extra_fields.setdefault('phone_number', 2222)
        extra_fields.setdefault('department', 'TI')
        extra_fields.setdefault('sid', '987654321')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            # last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('phone_number', 1111)
        extra_fields.setdefault('department', 'IT')
        extra_fields.setdefault('sid', '123456789')
        user = self._create_user(email, password, True, True, **extra_fields)

        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    sid = models.IntegerField(primary_key=True, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254)
    phone_number = models.IntegerField()
    profile_pic = models.ImageField(blank=True, upload_to="profile/")
    
    department = models.CharField(max_length=100)
    facebook_profile = models.URLField(null=True, blank=True)
    id_card_pic = models.ImageField(blank = True, null = True, upload_to = "id_card/")

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []
    # print("ok")
    objects = CustomUserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    def get_email(self):
        return self.email

    def __str__(self):
        return str(self.email)



class Catagory(models.Model):
    id = models.AutoField(primary_key=True)
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image1 = models.ImageField()
    image2 = models.ImageField(null = True)
    image3 = models.ImageField(null = True)
    original_url = models.URLField(blank=True, null=True)
    negotiable = models.BooleanField(default=True)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    details = models.TextField(max_length=10000, default = "Description")

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=5000)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text[:10])


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length= 2000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:10]
