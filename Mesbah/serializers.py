from rest_framework import serializers

from Mesbah.models import Clip, News, Podcast

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ['title', 'url']


class ClipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clip
        fields = ['title', 'url', 'cover']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'description', 'url', 'cover']        
