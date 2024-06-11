from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from Mesbah.models import Book, Clip, ImageAlbum, News, Podcast
from Mesbah.permissions import IsAdminOrReadOnly
from Mesbah.serializers import BookSerializer, ClipSerializer, ImageAlbumSerializer, NewsSerializer, PodcastSerializer 


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

class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAdminOrReadOnly]

class ImageAlbumViewSet(ModelViewSet):
    serializer_class = ImageAlbumSerializer
    queryset = ImageAlbum.objects.all()
    permission_classes = [IsAdminOrReadOnly]    