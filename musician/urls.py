from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MusicianViewSet

app_name = "musician"

router = DefaultRouter()
router.register("musicians", MusicianViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]
