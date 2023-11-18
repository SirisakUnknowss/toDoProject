from django.contrib import admin
# Project
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'completed', 'dueDate']
