from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'birthday']
    # fields = ['username', 'birthday']
    # exclude = ['username', 'birthday']
    ordering = ['birthday']
    search_fields = ['email', 'username']
