from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    """Модель пользователя"""

    avatar_url = models.CharField(verbose_name='URL фотографии пользователя', 
                                  max_length=256, 
                                  blank=True, 
                                  null=True)

    def __str__(self):
        return '{} {}'.format(self.username, self.first_name)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'