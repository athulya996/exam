from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Login(AbstractUser):
    is_user = models.BooleanField(default=False)
