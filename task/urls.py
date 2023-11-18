# Django
from django.urls import path
# Project
from . import views

urlpatterns = [
    path('add', views.AddTask.as_view(), name='addTaskApi'),
    path('edit', views.EditTask.as_view(), name='editTaskApi'),
    path('remove', views.RemoveTask.as_view(), name='removeTaskApi'),
]