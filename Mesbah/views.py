from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from Mesbah.models import Clip, News, Podcast
from Mesbah.permissions import IsAdminOrReadOnly
from Mesbah.serializers import ClipSerializer, NewsSerializer, PodcastSerializer 


class PodcastViewSet(ModelViewSet):

    serializer_class = PodcastSerializer
    queryset = Podcast.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class ClipViewSet(ModelViewSet):
    serializer_class = ClipSerializer
    queryset = Clip.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class NewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    permission_classes = [IsAdminOrReadOnly]    
