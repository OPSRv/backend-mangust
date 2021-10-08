from django.db import models
from django.utils import timezone


def upload_to(instance, filename):
    return f'article/{filename}'.format(filename=filename)


def upload_to_detail(instance, filename):
    return f'article/detail/{filename}'.format(filename=filename)


class ArticleDetail(models.Model):
    paragraph_1 = models.TextField(blank=False, verbose_name='Абзац_1')
    image_1 = models.ImageField(verbose_name="Зображення до абзацу 1", upload_to=upload_to_detail, blank=True)
    paragraph_2 = models.TextField(blank=True, verbose_name='Абзац_2')
    image_2 = models.ImageField(verbose_name="Зображення до абзацу 2", upload_to=upload_to_detail, blank=True)
    paragraph_3 = models.TextField(blank=True, verbose_name='Абзац_3')
    image_3 = models.ImageField(verbose_name="Зображення до абзацу 3", upload_to=upload_to_detail, blank=True)
    paragraph_4 = models.TextField(blank=True, verbose_name='Абзац_4')
    image_4 = models.ImageField(verbose_name="Зображення до абзацу", upload_to=upload_to_detail, blank=True)
    paragraph_5 = models.TextField(blank=True, verbose_name='Абзац_5')
    image_5 = models.ImageField(verbose_name="Зображення до абзацу 5", upload_to=upload_to_detail, blank=True)
    paragraph_6 = models.TextField(blank=True, verbose_name='Абзац_6')
    image_6 = models.ImageField(verbose_name="Зображення до абзацу 6", upload_to=upload_to_detail, blank=True)
    paragraph_7 = models.TextField(blank=True, verbose_name='Абзац_7')
    image_7 = models.ImageField(verbose_name="Зображення до абзацу 7", upload_to=upload_to_detail, blank=True)
    paragraph_8 = models.TextField(blank=True, verbose_name='Абзац_8')
    image_8 = models.ImageField(verbose_name="Зображення до абзацу 8", upload_to=upload_to_detail, blank=True)
    paragraph_9 = models.TextField(blank=True, verbose_name='Абзац_9')
    image_9 = models.ImageField(verbose_name="Зображення до абзацу 9", upload_to=upload_to_detail, blank=True)
    paragraph_10 = models.TextField(blank=True, verbose_name='Абзац_10')
    image_10 = models.ImageField(verbose_name="Зображення до абзацу 10", upload_to=upload_to_detail, blank=True)
    paragraph_11 = models.TextField(blank=True, verbose_name='Абзац_11')
    image_11 = models.ImageField(verbose_name="Зображення до абзацу 11", upload_to=upload_to_detail, blank=True)
    paragraph_12 = models.TextField(blank=True, verbose_name='Абзац_12')
    image_12 = models.ImageField(verbose_name="Зображення до абзацу 12", upload_to=upload_to_detail, blank=True)
    paragraph_13 = models.TextField(blank=True, verbose_name='Абзац_13')
    image_13 = models.ImageField(verbose_name="Зображення до абзацу 13", upload_to=upload_to_detail, blank=True)
    paragraph_14 = models.TextField(blank=True, verbose_name='Абзац_14')
    image_14 = models.ImageField(verbose_name="Зображення до абзацу 14", upload_to=upload_to_detail, blank=True)

    def __str__(self):
        return self.paragraph_1

    class Meta:
        ordering = ('-paragraph_1',)
        verbose_name = "Текст"
        verbose_name_plural = "Тексти"


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ('-last_name',)
        verbose_name = "Автор"
        verbose_name_plural = "Автори"


class Category(models.Model):
    categories = models.CharField(max_length=30)

    def __str__(self):
        return self.categories

    class Meta:
        ordering = ('categories',)
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Article(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    title = models.CharField(max_length=100, blank=False, verbose_name='Заголовок')
    image = models.ImageField(verbose_name="Зображення до статті", upload_to=upload_to, blank=True)

    paragraphs = models.ForeignKey(ArticleDetail, blank=True, on_delete=models.CASCADE, related_name='articles')
    author = models.ForeignKey(Author, blank=True, on_delete=models.CASCADE, related_name='articles')
    categories = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE, related_name='articles')

    publish = models.DateTimeField(default=timezone.now, verbose_name='Опубліковано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Змінено')
    status = models.BooleanField(verbose_name='Публікувати')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    owner = models.ForeignKey('auth.User', related_name='article', on_delete=models.CASCADE, verbose_name='Публікував')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-publish',)
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"
