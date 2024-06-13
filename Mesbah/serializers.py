from rest_framework import serializers

from Mesbah.models import Auditory, Book, Clip, ContactUs, Image, ImageAlbum, Martyr, News, Podcast

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



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'publish_date', 'image']         


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'images']


class ImageAlbumSerializer(serializers.ModelSerializer):

    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = ImageAlbum
        fields = ['title', 'image', 'images']


class MartyrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Martyr
        fields = ['name', 'description', 'cover', 'datetime_created']

class AuditorySerializer(serializers.ModelSerializer):
    class Meta:
         model = Auditory
         fields = ['title', 'cover', 'url', 'datetime_created']

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
         model = ContactUs
         fields = '__all__'
