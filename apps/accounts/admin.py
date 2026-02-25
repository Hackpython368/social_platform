from django.contrib import admin
from .models import User,Profile


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'is_active', 'is_staff')

# Register your models here.
admin.site.register(User,CustomUserAdmin)
admin.site.register(Profile)