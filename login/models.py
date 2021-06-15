from django.db import models


class Profile(models.Model):
    """Модель пользователя """
    
    name_user = models.CharField(verbose_name='Имя пользователя', max_length=100)
    photo_user = models.ImageField(verbose_name='Фотография пользователя', upload_to='media/photo_user/')
    
