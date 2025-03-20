from django.urls import path

from . import views

app_name = "miapp"

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("create_post/", views.create_post, name="create_post"),
]
