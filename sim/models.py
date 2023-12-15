from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
