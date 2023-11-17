import uuid

from django.db import models


class Farm(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4())
    title = models.CharField(max_length=50, default='Farm')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'farm'
        ordering = ['-created_at']


class UserFarmLink(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4())
    user = models.CharField(max_length=50, default='user')
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='user_farm_link_farm')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_farm_link'
        ordering = ['-created_at']
