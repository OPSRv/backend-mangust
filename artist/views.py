
from rest_framework import generics
from . import serializers
from .models import MusicBand


class MusicBandList(generics.ListAPIView):
    queryset = MusicBand.objects.all()
    serializer_class = serializers.MusicBandSerializer


class MusicBandDetail(generics.RetrieveAPIView):
    queryset = MusicBand.objects.all()
    serializer_class = serializers.MusicBandSerializerDetail
