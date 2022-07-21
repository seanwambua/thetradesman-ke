from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Buyer(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    intro = models.CharField(max_length=255, null=True, blank=True)
    date_time_created = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='buyer', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name', 'date_time_created']

    def __str__(self):
        return self.name
