# from datetime import datetime
# import pytz
from django.db import models
from config import settings
# from django.utils import timezone


NULLABLE = {'null': 'True', 'blank': 'True'}
USER = settings.AUTH_USER_MODEL


# zone = pytz.timezone(settings.TIME_ZONE)
# current_datetime = datetime.now(zone)


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='контактный email')
    name = models.CharField(max_length=100, verbose_name="Ф. И. О.", **NULLABLE)
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)
    owner = models.ForeignKey(USER, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('email',)


class Message(models.Model):
    theme = models.CharField(max_length=100, verbose_name='тема письма')
    text = models.TextField(verbose_name='текст письма')
    owner = models.ForeignKey(USER, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.theme}'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'
        ordering = ('theme',)

# class Mailing(models.Model):
#     sent_at = models.DateTimeField(verbose_name='дата и время первой отправки', **NULLABLE)
#     period_choices = {'раз в день': 'раз в день', 'раз в неделю': 'раз в неделю', 'раз в месяц': 'раз в месяц'}
#     period = models.CharField(max_length=15, choices=period_choices, default='раз в день', verbose_name='периодичность')
#     status_choices = {'created': 'создана', 'executing': 'запущена', 'finished': 'завершена'}
#     status = models.CharField(max_length=15, choices=status_choices, default="создана", verbose_name='статус')
#     message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение', **NULLABLE)
#     clients = models.ManyToManyField(Client, verbose_name='клиенты')
#     owner = models.ForeignKey(USER, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
#     start_at = models.DateTimeField(default=timezone.now, verbose_name='дата старта')
#     finish_at = models.DateTimeField(default=current_datetime + timedelta(days=7), verbose_name='дата окончания')
#     is_active = models.BooleanField(default=True, verbose_name='активна')
#
#     def __str__(self):
#         return f'{self.message}'
#
#     class Meta:
#         verbose_name = 'рассылка'
#         verbose_name_plural = 'рассылки'
#         ordering = ('sent_at',)
