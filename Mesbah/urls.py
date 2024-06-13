from django.urls import include, path
# from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('podcasts', views.PodcastViewSet, basename='podcast')
router.register('clips', views.ClipViewSet, basename='clip')
router.register('news', views.NewsViewSet, basename='news')
router.register('books', views.BookViewSet, basename='books')
router.register('albums', views.ImageAlbumViewSet, basename='albums')
router.register('contactus', views.ContactUsViewSet, basename='contactus')
router.register('martyr', views.MartyrViewSet, basename='martyr')
router.register('audio', views.AuditoryViewSet, basename='audio')


urlpatterns = router.urls



