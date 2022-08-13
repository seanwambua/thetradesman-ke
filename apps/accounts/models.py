from PIL import Image
from django.contrib.auth.models import User
from django.core.files import File
from django.db import models


class UserRole(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return self.title


class UserAccount(models.Model):
    name = models.CharField(max_length=40)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    introduction = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    user_role = models.ForeignKey(UserRole, related_name="roles", on_delete=models.CASCADE)

    image = models.ImageField(upload_to='profile/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='profile/', blank=True, null=True)

    class Meta:
        ordering = ['name', 'created']

    def __str__(self):
        return self.name
