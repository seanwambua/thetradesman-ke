from django.contrib import admin
from apps.store.models import Category, DeliveryPeriod, Policy, Products

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug':('title',)} 
    
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'slug', 'created' ,'updated']
    prepopulated_fields = {'slug':('title',)}
    list_filter=['is_stock', 'is_active']
    list_editable= ['title', 'description','price', ]

@admin.register(DeliveryPeriod)
class DeliveryPeriodAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug':('title',)} 

@admin.register(Policy)
class ProductPolicyAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug':('title',)} 

