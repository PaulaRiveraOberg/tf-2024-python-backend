from django.contrib import admin
from django.urls import include, path
#from oauthserverapp import views #bloqueB
from myapp import views #bloqueA
from django.contrib.auth.views import LogoutView
#from oauth2_provider import urls as oauth2_urls #bloque B

urlpatterns = [
    path("", views.home, name="home"),
    path('admin/', admin.site.urls),  # Panel de administración
    path('auth/', include('social_django.urls', namespace='social')),  # URLs para autenticación OAuth
    path('profile/', views.profile, name='profile'),  # Página de perfil del usuario
    path('logout/', LogoutView.as_view(), name='logout'),  # Cierre de sesión

    #path("o/", include(oauth2_urls)),
    #path("secret-resource/", views.SecretMessageView.as_view(), name="secret-resource"),

]
