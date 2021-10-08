from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Article, ArticleDetail, Author, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'get_image', 'status')
    list_filter = ('created', 'publish', 'owner')
    list_display_links = ('title',)
    search_fields = ('body',)
    readonly_fields = ('get_image',)
    date_hierarchy = 'publish'

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="128" height="96">')

    get_image.short_description = 'Зображення'



@admin.register(ArticleDetail)
class ArticleDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'paragraph_1', 'get_image')
    list_display_links = ('paragraph_1',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image_1.url} width="128" height="96">')

    get_image.short_description = 'Фото'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', )
    list_display_links = ('first_name', 'last_name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'categories',)
    list_display_links = ('categories',)

