from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Release, Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_image')
    list_display_links = ('title',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="128" height="96">')

    get_image.short_description = 'Зображення'


@admin.register(Release)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'program', 'description', 'created', 'quantity', 'status')
    list_display_links = ('title',)
