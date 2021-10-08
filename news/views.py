from rest_framework import generics
from .serializers import ArticleSerializer, ArticleSerializerDetail
from .models import Article


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.filter(status=True)
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveAPIView):
    queryset = Article.objects.filter(status=True)
    serializer_class = ArticleSerializerDetail
