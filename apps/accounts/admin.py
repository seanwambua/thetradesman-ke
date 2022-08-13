from django.contrib import admin

from apps.accounts.models import UserRole, UserAccount


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['name']
