from django.urls import include, path
from rest_framework import routers

from .views import MyPostViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"my-posts", MyPostViewSet, basename="my-posts")

urlpatterns = [
    path("", include(router.urls)),
]
