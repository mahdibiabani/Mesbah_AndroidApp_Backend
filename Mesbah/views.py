from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework import generics
from Mesbah.models import Auditory, Book, Clip, ContactUs, ImageAlbum, Martyr, News, Podcast
from Mesbah.permissions import IsAdminOrReadOnly
from Mesbah.serializers import AuditorySerializer, BookSerializer, ClipSerializer, ContactUsSerializer, ImageAlbumSerializer, MartyrSerializer, NewsSerializer, PodcastSerializer 


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

class MartyrViewSet(ModelViewSet):
    serializer_class = MartyrSerializer
    queryset = Martyr.objects.all()
    permission_classes = [IsAdminOrReadOnly]

class AuditoryViewSet(ModelViewSet):
    serializer_class = AuditorySerializer
    queryset = Auditory.objects.all()    
    permission_classes = [IsAdminOrReadOnly]

class ContactUsViewSet(ModelViewSet):
    http_method_names = ['post']
    serializer_class = ContactUsSerializer
    queryset = ContactUs.objects.all()
    
   

        

