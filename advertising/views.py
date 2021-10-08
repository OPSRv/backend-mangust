from rest_framework import generics
from . import serializers
from .models import Advertising

class AdvertisingList(generics.ListAPIView):
    queryset = Advertising.objects.all()
    serializer_class = serializers.AdvertisingSerializer