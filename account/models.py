from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):

    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    username    = models.CharField(max_length=50, null=True, blank=True)
    email       = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.user.pk