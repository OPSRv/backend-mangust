from django.db import models


def upload_to(instance, filename):
    return f'music_band/{filename}'.format(filename=filename)


class MusicBand(models.Model):
    name = models.CharField(max_length=100, blank=False, default='', verbose_name="Назва колективу")
    music_styles = models.CharField(max_length=100, blank=False, default='', verbose_name="Музичний стиль")
    about_band = models.TextField(blank=False, default='', verbose_name="Інформація про колектив")
    logo = models.ImageField(verbose_name="Логотип", upload_to="music_band")
    instagram_link = models.CharField(max_length=256, blank=True, default='', verbose_name="Посилання на Instagram")
    facebook_link = models.CharField(max_length=256, blank=True, default='', verbose_name="Посилання на FaceBook")
    youtube_link = models.CharField(max_length=256, blank=True, default='', verbose_name="Посилання на Youtube")
    telegram_link = models.CharField(max_length=128, blank=True, default='', verbose_name="Посилання на Telegram")
    soundcloud_link = models.CharField(max_length=128, blank=True, default='', verbose_name="Посилання на SoundCloud")
    mobile_number = models.CharField(max_length=16, blank=True, default='', verbose_name="Номер телефону")
    email_band = models.EmailField(verbose_name="Електронна пошта")
    last_songs_link_1 = models.CharField(max_length=256, blank=True, default='', verbose_name="Реліз_1")
    last_songs_link_2 = models.CharField(max_length=256, blank=True, default='', verbose_name="Реліз_2")
    last_songs_link_3 = models.CharField(max_length=256, blank=True, default='', verbose_name="Реліз_3")
    last_songs_link_4 = models.CharField(max_length=256, blank=True, default='', verbose_name="Реліз_4")
    last_songs_link_5 = models.CharField(max_length=256, blank=True, default='', verbose_name="Реліз_5")
    last_songs_link_6 = models.CharField(max_length=256, blank=True, default='', verbose_name="Реліз_6")
    last_songs_link_7 = models.CharField(max_length=256, blank=True, default='', verbose_name="Реліз_7")
    last_songs_link_8 = models.CharField(max_length=256, blank=True, default='', verbose_name="Реліз_8")

    class Meta:
        ordering = ['id']
        verbose_name = "Виконавця"
        verbose_name_plural = "Виконавці"

    def __str__(self):
        return self.name
