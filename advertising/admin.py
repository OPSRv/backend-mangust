from django.contrib import admin

from .models import Advertising, Example


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('title',)


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'status')
    list_display_links = ('description',)


admin.site.site_title = "Man-Gust FM online radio"
admin.site.site_header = "Man-Gust FM online radio"
