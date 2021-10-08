from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Gallery

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'date', 'get_image')
    list_display_links = ('description',)
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="128" height="96"')

    get_image.short_description = 'Фото'
