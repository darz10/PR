from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    """Абстрактная модель пользователя"""

    avatar_url = models.CharField(verbose_name='URL фотографии пользователя', max_length=256, blank=True, null=True)

    def __str__(self):
        return self.first_name