from django.db import models

from config import settings
from users.models import User


class File(models.Model):
    STATUS = (
        ("CONFIRMED", "confirmed"),
        ("REJECTED", "rejected"),
        ("NONE", "none"),
    )

    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='static/files', verbose_name='файл')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='files', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default='NONE', max_length=100,
                              verbose_name='статус')
    is_send = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'файл'
        verbose_name_plural = 'Файлы'
