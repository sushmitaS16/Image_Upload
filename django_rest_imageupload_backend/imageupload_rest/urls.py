from django.conf.urls import url, include
from rest_framework import routers
from imageupload_rest.viewsets import UploadImageViewSet

router = routers.DefaultRouter()
router.register('images', UploadImageViewSet, 'images')

urlpatterns = [
    url(r'^', include(router.urls))
]
