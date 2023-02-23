from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tweet(models.Model):
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=5)
    email = models.EmailField(default='User@sample')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

