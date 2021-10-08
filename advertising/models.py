from django.db import models
from django.utils import timezone


def upload_to_audio(instance, filename):
    return f'advertising/audio/{filename}'.format(filename=filename)


class Advertising(models.Model):
    """Реклама"""
    title = models.CharField(max_length=100, blank=False, default='Замовити рекламу', verbose_name='Заголовок')
    description = models.TextField(max_length=100, blank=False, verbose_name='Опис')

    class Meta:
        ordering = ['title']
        verbose_name = "Заголовок"
        verbose_name_plural = "Заголовок реклами"

    def __str__(self):
        return self.description


class Example(models.Model):
    description = models.CharField(max_length=100, blank=False, default='Замовити рекламу', verbose_name='Короткий опис')
    advertising = models.ForeignKey(Advertising, blank=False, on_delete=models.CASCADE, related_name='examples')
    audio = models.FileField(upload_to=upload_to_audio, blank=True, default='', verbose_name='Аудіо файл')
    video = models.CharField(max_length=256, blank=True, default='', verbose_name='Відео файл')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Опубліковано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Змінено')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    status = models.BooleanField(verbose_name='Публікувати')
    owner = models.ForeignKey('auth.User', related_name='examples', on_delete=models.CASCADE, verbose_name='Публікував')

    class Meta:
        ordering = ['created']
        verbose_name = "Приклади реклами"
        verbose_name_plural = 'Приклади реклами'
