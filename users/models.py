from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):

    username = models.CharField(max_length=50, unique=True,)
    email = models.EmailField(unique=True, verbose_name='почта')
    full_name = models.CharField(max_length=150, verbose_name='полное имя', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='город', **NULLABLE)
    phone = models.CharField(max_length=15, verbose_name='телефон', **NULLABLE)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'