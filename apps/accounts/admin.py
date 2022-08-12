from django.contrib import admin

from .models import UserRole, UserAccount

admin.site.register(UserRole)


class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(UserAccount)


class AccountUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['is_staff', 'is_superuser']
    list_editable = ['name']
