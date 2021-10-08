from django.shortcuts import render
from rest_framework import generics
# from rest_framework.parsers import MultiPartParser, FormParser

from . import serializers
from .models import Gallery
from rest_framework.views import APIView


class GalleryList(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = serializers.GallerySerializer


class GalleryDetail(generics.RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = serializers.GallerySerializerDetail