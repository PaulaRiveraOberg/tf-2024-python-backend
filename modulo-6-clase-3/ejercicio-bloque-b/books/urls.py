from books.views import BibliotecaAPIView, SalaVIPAPIView
from django.urls import path

urlpatterns = [
    path("biblioteca/", BibliotecaAPIView.as_view(), name="biblioteca"),
    path("sala-vip/", SalaVIPAPIView.as_view(), name="sala-vip"),
]
