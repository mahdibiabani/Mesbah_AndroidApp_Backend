from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin
from Mesbah.models import Book, Clip, Image, ImageAlbum, News, Podcast



@admin.register(Podcast)
class PodcastAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'url']



@admin.register(Clip)
class ClipAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'url', 'cover']



@admin.register(News)
class NewsAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'url', 'cover', 'descripton']


class ImageAdmin(admin.TabularInline):
    model = Image

@admin.register(ImageAlbum)
class ImageAlbumAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    inlines = [ImageAdmin]
    list_display = ['title', 'image']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'author', 'publish_date', 'image']

