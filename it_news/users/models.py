from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    bio = models.TextField('Биография', blank=True)
    company = models.CharField('Коммпания', max_length=30, blank=True)
