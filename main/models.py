from django.db import models
from django.utils import timezone

from config import settings

NULLABLE = {'null': 'True', 'blank': 'True'}
USER = settings.AUTH_USER_MODEL


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='контактный email')
    name = models.CharField(max_length=100, verbose_name='Ф. И. О.', **NULLABLE)
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)
    owner = models.ForeignKey(USER, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('email',)


class Message(models.Model):
    theme = models.CharField(max_length=100, verbose_name='тема письма')
    text = models.TextField(verbose_name='текст письма')
    owner = models.ForeignKey(USER, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return f'Тема письма: {self.theme}'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'
        ordering = ('theme',)


class Mailing(models.Model):
    CHOICES_INTERVAL = [('day', 'раз в день'), ('week', 'раз в неделю'), ('month', 'раз в месяц')]
    STATUS_CHOICES = [('completed', 'Завершена'), ('created', 'Создана'), ('launched', 'Запущена')]

    periodicity = models.CharField(default='разовая', max_length=50,
                                   choices=CHOICES_INTERVAL, verbose_name='периодичность')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='статус рассылки', **NULLABLE)
    start_date = models.DateTimeField(default=timezone.now, verbose_name='дата начала')
    next_date = models.DateTimeField(default=timezone.now, verbose_name='следующая дата')
    end_date = models.DateTimeField(default=timezone.now, verbose_name='конечная дата')
    title = models.CharField(max_length=100, verbose_name='заголовок рассылки')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, null=True, verbose_name='сообщение')
    client = models.ManyToManyField(Client, verbose_name='клиенты')
    is_active = models.BooleanField(default=True, verbose_name='актуальная')
    owner = models.ForeignKey(USER, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return f'Рассылка {self.title}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('start_date',)


class Logs(models.Model):
    last_mailing_time = models.DateTimeField(auto_now=True, verbose_name='время последней попытки', **NULLABLE)
    status = models.CharField(max_length=50, verbose_name='статус попытки рассылки', null=True)
    response = models.CharField(max_length=255, verbose_name='ответ почтового сервера', **NULLABLE)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)

    def __str__(self):
        log = f'Попытка рассылки {self.mailing} {self.last_mailing_time} '
        if self.status:
            log += 'Успешная попытка отправки'
        else:
            log += f'Ошибка: {self.response}'
        return log

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = ('last_mailing_time',)
