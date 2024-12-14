# myproject/urls.py
from django.contrib import admin
from django.urls import path
from myapp.views import index, post_detail

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("post/<int:post_id>/", post_detail, name="post_detail"),
]
