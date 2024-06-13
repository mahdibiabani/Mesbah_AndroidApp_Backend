from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 
from Mesbah.utils import RandomFileName


class Podcast(models.Model):
    title = models.CharField(_('title'), max_length=500)
    url = models.FileField(_('url'), upload_to=RandomFileName("podcast_files"))
    datetime_created = models.DateTimeField(_('created'), default=timezone.now)
    datetime_modified = models.DateTimeField(_('modified'), auto_now=True)

    class Meta:
        verbose_name_plural = _('podcasts')

    class Meta:
        verbose_name = _('podcast')

    def __str__(self):
        return self.title


class Clip(models.Model):
    title = models.CharField(_('title'), max_length=500)
    url = models.FileField(_('url'), upload_to= RandomFileName("clip_files"))
    cover = models.ImageField(_('cover'), upload_to='clip/clip_cover', blank=True)
    datetime_created = models.DateTimeField(_('created'), default=timezone.now)
    datetime_modified = models.DateTimeField(_('modified'), auto_now=True)


    class Meta:
        verbose_name_plural = _('clips')

    def __str__(self):
        return self.title
    


class News(models.Model):
    title = models.CharField(_('title'), max_length=500)
    description = models.TextField(_('description'), )
    url = models.CharField(_('url'), max_length=500)
    cover = models.ImageField(_('cover'), upload_to='news/news_cover', blank=True)
    datetime_created = models.DateTimeField(_('created'), default=timezone.now)
    datetime_modified = models.DateTimeField(_('modified'), auto_now=True)


    class Meta:
        verbose_name_plural = _('news')

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), )
    author = models.CharField(_('author'), max_length=255)
    publish_date = models.CharField(_('publish_date'), max_length=255)
    image = models.ImageField(_('image'), upload_to='book/book_cover', blank=True)

    datetime_created = models.DateTimeField(_('created'), default=timezone.now)
    datetime_modified = models.DateTimeField(_('modified'), auto_now=True)


    class Meta:
        verbose_name_plural = _('books')

    def __str__(self):
        return self.title
    

class ImageAlbum(models.Model):
    title = models.CharField(_('title'), max_length=255)   
    image = models.ImageField(_('image'), upload_to='album/album_cover', blank=True)

    datetime_created = models.DateTimeField(_('created'), default=timezone.now)
    datetime_modified = models.DateTimeField(_('modified'), auto_now=True)

    class Meta:
        verbose_name_plural = _('images album')


    def __str__(self):
        return self.title



class Image(models.Model):
    images = models.ImageField(_('images'), upload_to="product-images", default="product.jpg")
    album = models.ForeignKey(ImageAlbum, related_name="images", on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(_('created'), auto_now_add=True)

    class Meta:
        verbose_name_plural = _("Album Images")



class Martyr(models.Model):
    name = models.CharField(_('name'), max_length=500)
    description = models.TextField(_('description'), )
    cover = models.ImageField(_('cover'), upload_to='martyr/martyr_cover', blank=True)
    datetime_created = models.DateTimeField(_('created'), default=timezone.now)


    class Meta:
        verbose_name_plural = _('martyrs')


    def __str__(self):
        return self.name

class Auditory(models.Model):
    title = models.CharField(_('title'), max_length=500)
    cover = models.ImageField(_('cover'), upload_to='audio/audio_cover', blank=True)
    url = models.FileField(_('url'), upload_to= RandomFileName("audio_files"))
    datetime_created = models.DateTimeField(_('created'), default=timezone.now)

    class Meta:
        verbose_name_plural = _('auditories')    

    def __str__(self):
        return self.title
    

class ContactUs(models.Model):
    identity = models.CharField(_('identity'), max_length=500, blank=True)
    subject = models.CharField(_('subject'), max_length=500)
    message = models.TextField(_('message'), )
    datetime_created = models.DateTimeField(_('created'), auto_now_add=True)


    class Meta:
        verbose_name_plural = _("contact us")

    def __str__(self):
        return self.subject






