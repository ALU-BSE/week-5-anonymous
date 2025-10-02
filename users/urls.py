from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import (
    UserViewSet,
    PassengerViewSet,
    RiderViewSet,
    RegisterView,
    LoginView,
    UserProfileView,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'passengers', PassengerViewSet, basename='passenger')
router.register(r'riders', RiderViewSet, basename='rider')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='profile'),
] + router.urls