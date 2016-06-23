from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class backuser(AbstractUser):
    area = models.CharField(max_length=30)


