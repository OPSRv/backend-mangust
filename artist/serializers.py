from rest_framework import serializers
from .models import MusicBand


class MusicBandSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicBand
        fields = ['id', 'name', 'logo']


class MusicBandSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = MusicBand
        fields = ['id', 'name', 'music_styles', 'about_band', 'logo', 'instagram_link', 'facebook_link', 'youtube_link',
                  'telegram_link', 'soundcloud_link', 'mobile_number', 'email_band', 'last_songs_link_1',
                  'last_songs_link_2', 'last_songs_link_3', 'last_songs_link_4', 'last_songs_link_5',
                  'last_songs_link_6',
                  'last_songs_link_7', 'last_songs_link_8']
