from rest_framework import serializers
from .models import Advertising, Example


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ('audio', 'video')


class AdvertisingSerializer(serializers.ModelSerializer):
    examples = ExampleSerializer(many=True, read_only=True)

    class Meta:
        model = Advertising
        fields = ('id', 'title', 'description', 'examples')