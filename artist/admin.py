from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import MusicBand


@admin.register(MusicBand)
class MusicBandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_image')
    list_display_links = ('name',)
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.logo.url} width="128" height="128"')

    get_image.short_description = 'Лого'
