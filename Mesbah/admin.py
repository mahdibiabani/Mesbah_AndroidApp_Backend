from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin
from Mesbah.models import Auditory, Book, Clip, ContactUs, Image, ImageAlbum, Martyr, News, Podcast



@admin.register(Podcast)
class PodcastAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'url']



@admin.register(Clip)
class ClipAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'url', 'cover']



@admin.register(News)
class NewsAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'url', 'cover', 'description']


class ImageAdmin(admin.TabularInline):
    model = Image

@admin.register(ImageAlbum)
class ImageAlbumAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    inlines = [ImageAdmin]
    list_display = ['title', 'image']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'author', 'publish_date', 'image']

@admin.register(Martyr)
class MartyrAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'cover', 'datetime_created']


@admin.register(Auditory)
class Auditory(admin.ModelAdmin):
    list_display = ['title', 'cover', 'url', 'datetime_created']


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['identity', 'subject', 'message', 'datetime_created']
    readonly_fields = ['identity', 'subject', 'message', 'datetime_created']