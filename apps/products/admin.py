from django.contrib import admin

from apps.products.models import Category, Products

admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     list_display = ['name', 'slug']
     prepopulated_fields = {'slug':('title',)} 
    
admin.site.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'slug', 'created' ,'updated']
    prepopulated_fields = {'slug':('title',)}
    list_filter=['in_stock', 'is_active']
    list_editable= ['price', 'description', 'title']