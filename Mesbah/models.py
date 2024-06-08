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


