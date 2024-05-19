from datetime import datetime

import pytz
from django.db import models

from config import settings

NULLABLE = {'null': 'True', 'blank': 'True'}
zone = pytz.timezone(settings.TIME_ZONE)
current_datetime = datetime.now(zone)


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='почта')
    comment = models.CharField(max_length=100, verbose_name='комментарий', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь',
                              **NULLABLE)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('email',)
