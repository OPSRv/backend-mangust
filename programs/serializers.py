from rest_framework import serializers

from .models import Program, Release


class ReleasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        exclude = ('updated', 'status', 'program', 'owner', 'publish')


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'


class ProgramSerializerDetail(serializers.ModelSerializer):
    releases = ReleasesSerializer(many=True, read_only=True)

    class Meta:
        model = Program
        fields = ('title', 'releases',)
