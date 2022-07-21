from django.contrib import admin

from apps.products.models import Category, Products

admin.site.register(Category)
admin.site.register(Products)
