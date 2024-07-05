from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(verbose_name="이름", max_length=50)
    email = models.EmailField(verbose_name="Email", max_length=100)
    birthday = models.DateField(verbose_name="생년월일", null=True, blank=True)

    def __str__(self):
        return self.name