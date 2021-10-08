from rest_framework import serializers

from .models import Article, ArticleDetail, Author, Category


class ArticleParagraphsSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = ArticleDetail
        exclude = ('id',)


class ArticleSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(slug_field='categories', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'image', 'categories', 'publish',)


class ArticleSerializerDetail(serializers.ModelSerializer):
    paragraphs = ArticleParagraphsSerializerDetail(required=False)
    author = serializers.SlugRelatedField(slug_field='first_name', read_only=True)
    categories = serializers.SlugRelatedField(slug_field='categories', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'image', 'author', 'categories', 'publish', 'paragraphs')
