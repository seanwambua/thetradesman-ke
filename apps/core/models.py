"""
from django.db import models
from apps.accounts.models import UserAccount

class Cart(models.Model):
    title = models.CharField(max_length=255, default=0, null=False)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    buyer = models.ForeignKey(UserAccount, related_name="buyer", on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title# Create your models here.
"""