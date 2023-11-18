from django.db import models

# Create your models here.

class Task(models.Model):
    user        = models.ForeignKey(to='account.Account', null=True, blank=True, on_delete=models.CASCADE, related_name='accountTodoTask')
    name        = models.CharField(max_length=100, null=True, blank=True)
    detail      = models.CharField(max_length=100, null=True, blank=True)
    completed   = models.BooleanField(default=False)
    created     = models.DateTimeField(auto_now=True)
    dueDate     = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.user}"