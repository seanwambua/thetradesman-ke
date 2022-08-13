from django.contrib import admin

from apps.accounts.models import UserRole, CustomUser


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['name']
