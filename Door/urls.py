from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from .views import DoorViewSet

router = routers.DefaultRouter()
router.register('door', DoorViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
