from rest_framework import serializers
from .models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'date', 'photo']


class GallerySerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'date', 'photo', 'description', 'topic']
