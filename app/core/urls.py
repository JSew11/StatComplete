from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views.user_registration_viewset import UserRegistrationViewSet
from .views.user_field_validation_views import check_username_available

app_name = 'core'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationViewSet.as_view(), name='register'),
    path('check_username/', check_username_available, name='check_username')
]