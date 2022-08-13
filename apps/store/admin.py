from django.contrib import admin

from apps.store.models import Category, DeliveryPeriod, Policy, Products, Services


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description', 'price', 'created', 'updated']
    list_display_links = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['in_stock', 'is_active']
    list_editable = ['description', 'price', ]


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['is_active']
    list_editable = ['description', 'price', ]


@admin.register(DeliveryPeriod)
class DeliveryPeriodAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Policy)
class ProductPolicyAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
