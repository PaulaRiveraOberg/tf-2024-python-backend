"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from myapp.views import MiVista, ProductoView, ProductoViewFiltered, ProductoListView, ProductoDetailView
from django.views.generic import ListView
from myapp.models import Producto

urlpatterns = [
    path("admin/", admin.site.urls),
    path("mi-vista/", MiVista.as_view()),
    path("productos/", ProductoView.as_view()),
    path("productos-filtrados/", ProductoViewFiltered.as_view()),
    path("productos-list/", ProductoListView.as_view(), name="productos-lista"),
    path("productos-list-2/", ListView.as_view(model=Producto, template_name="lista.html", context_object_name="productos"), name="productos-lista"),
    path("productos-detalle/<int:pk>/", ProductoDetailView.as_view(), name="productos-detalle"),
]
