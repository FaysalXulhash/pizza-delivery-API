from django.contrib import admin
from .models import Account

@admin.register(Account)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'phone_number', 'date_joined', 'last_login', 'is_active')
    fields = ('email', 'username', 'phone_number', 'password')
    # list_display_links = ('email', ' username', 'phone_number',)
    readonly_fields = ('date_joined', 'last_login',)
    ordering = ['-date_joined']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

