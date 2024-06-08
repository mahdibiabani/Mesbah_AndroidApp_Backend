from django.urls import include, path
# from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('podcasts', views.PodcastViewSet, basename='podcast')
router.register('clips', views.ClipViewSet, basename='clip')
router.register('news', views.NewsViewSet, basename='news')


urlpatterns = router.urls

