from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    phone = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username