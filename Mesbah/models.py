from django.db import models
from django.utils import timezone

from Mesbah.utils import RandomFileName


class Podcast(models.Model):
    title = models.CharField(max_length=500)
    url = models.FileField(upload_to=RandomFileName("podcast_files"),verbose_name="url")
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Clip(models.Model):
    title = models.CharField(max_length=500)
    url = models.FileField(upload_to= RandomFileName("clip_files"),verbose_name="url")
    cover = models.ImageField(upload_to='clip/clip_cover', blank=True)
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    


class News(models.Model):
    title = models.CharField(max_length=500)
    descripton = models.TextField()
    url = models.CharField(max_length=500)
    cover = models.ImageField(upload_to='news/news_cover', blank=True)
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    publish_date = models.CharField(max_length=255)
    image = models.ImageField(upload_to='book/book_cover', blank=True)

    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class ImageAlbum(models.Model):
    title = models.CharField(max_length=255)   
    image = models.ImageField(upload_to='album/album_cover', blank=True)

    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title



class Image(models.Model):
    images = models.ImageField(upload_to="product-images", default="product.jpg")
    album = models.ForeignKey(ImageAlbum, related_name="images", on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Album Images"