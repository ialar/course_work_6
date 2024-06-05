from django.db import models
from django.utils import timezone

NULLABLE = {'null': 'True', 'blank': 'True'}


class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое статьи', **NULLABLE)
    preview = models.ImageField(upload_to='blogpost_images/', verbose_name='изображение', **NULLABLE)
    views = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='дата публикации')

    def __str__(self):
        return f'"{self.title}" (дата создания: {self.created_at})'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ('created_at',)
