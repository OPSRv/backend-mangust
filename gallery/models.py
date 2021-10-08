from django.db import models


def upload_to(instance, filename):
    return f'gallery/{filename}'.format(filename=filename)


class Gallery(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(verbose_name="Завантаження фото", upload_to=upload_to,
                              default='gallery/default.jpg')
    description = models.CharField(max_length=256, blank=False, default='', verbose_name="Опис фото")
    topic = models.CharField(max_length=32, blank=False, default='', verbose_name="Тематика")

    class Meta:
        ordering = ['date']
        verbose_name = "Зображення"
        verbose_name_plural = "Галерея"

    def __str__(self):
        return self.description
