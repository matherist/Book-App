from rest_framework import serializers
from .models import YouTube


class YouTubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTube
        fields = ['title', 'description', 'link']