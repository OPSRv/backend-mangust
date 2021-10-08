from django.db import models
from django.utils import timezone

from news.models import Author, Category


def upload_to_images(instance, filename):
    return f'programs/{filename}'.format(filename=filename)


def upload_to_audio(instance, filename):
    return f'programs/audio/{filename}'.format(filename=filename)


class Program(models.Model):
    author = models.ForeignKey(Author, blank=True, on_delete=models.CASCADE, related_name='programs')
    category = models.ForeignKey(Category, blank=False, on_delete=models.CASCADE, related_name='programs')

    title = models.CharField(max_length=100, blank=False, verbose_name='Назва програим')
    description = models.TextField(max_length=100, blank=False, verbose_name='Короткий опис')
    image = models.ImageField(verbose_name="Зображення до програми')", upload_to=upload_to_images, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-title',)
        verbose_name = "Программа"
        verbose_name_plural = "Программи"


class Release(models.Model):
    program = models.ForeignKey(Program, blank=False, on_delete=models.CASCADE, related_name='releases')
    quantity = models.IntegerField(default=0, verbose_name='Кількість переглядів')
    audio_file = models.FileField(upload_to=upload_to_audio, blank=True, verbose_name='Аудіо файл')
    title = models.CharField(max_length=100, blank=False, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Опис до випуску')

    publish = models.DateTimeField(default=timezone.now, verbose_name='Опубліковано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Змінено')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    status = models.BooleanField(verbose_name='Публікувати')
    owner = models.ForeignKey('auth.User', related_name='release', on_delete=models.CASCADE, verbose_name='Публікував')

    def __str__(self):
        return self.description

    class Meta:
        ordering = ('-description',)
        verbose_name = "Реліз"
        verbose_name_plural = "Релізи"
