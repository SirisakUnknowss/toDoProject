from django.contrib import admin
# Project
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):

    list_display = ['id', 'username', 'email']
