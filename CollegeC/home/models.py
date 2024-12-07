from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .manegers import *

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    address  = models.CharField(max_length=120)
    userImg = models.ImageField(blank=True, null=True)  # Image upload is optional
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)     
    is_normal_user = models.BooleanField(default=False)     
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)       
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        db_table = "CustomUser"