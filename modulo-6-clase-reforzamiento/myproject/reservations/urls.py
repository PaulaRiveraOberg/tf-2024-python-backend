from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, ReservationViewSet, TokenProtectedViewSet, JWTProtectedViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'reservations-basic', ReservationViewSet, basename='reservations-basic')
router.register(r'reservations-token', TokenProtectedViewSet, basename='reservations-token')
router.register(r'reservations-jwt', JWTProtectedViewSet, basename='reservations-jwt')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),  # Token Auth estándar de DRF
    path('jwt-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT Login
    path('jwt-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]