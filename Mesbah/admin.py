from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin
from Mesbah.models import Clip, News, Podcast



@admin.register(Podcast)
class PodcastAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'url']



@admin.register(Clip)
class ClipAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'url', 'cover']



@admin.register(News)
class NewsAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'url', 'cover', 'descripton']



