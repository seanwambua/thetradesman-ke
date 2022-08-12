from django.contrib import admin
from .models import AccountType, AccountUser


admin.site.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
     list_display = ['title', 'slug']
     prepopulated_fields = {'slug':('title',)} 

admin.site.register(AccountUser)
class AccountUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)} 
    list_filter=['is_staff', 'is_superuser']
    list_editable= ['name']