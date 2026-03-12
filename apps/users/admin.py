from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'role', 'is_active', 'is_blocked')
    fieldsets = UserAdmin.fieldsets + ((
        'Platform Data',
        {'fields': ('phone', 'role', 'is_blocked')},
    ),)
