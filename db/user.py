import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    last_login = None
    is_active = None
    is_superuser = None
    is_staff = None
    date_joined = None

    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4())
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=12, unique=True)
    is_active = models.BooleanField(default=False)
    profile_pic = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'
        ordering = ['first_name']

    @property
    def fullname(self):
        if self.last_name is None:
            return self.first_name
        return f"{self.first_name} {self.last_name}"


class Farm(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4())
    title = models.CharField(max_length=50, default='Farm')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'farm'
        ordering = ['-created_at']


class UserFarmLink(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4())
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_farm_link_user')
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='user_farm_link_farm')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_farm_link'
        ordering = ['-created_at']
