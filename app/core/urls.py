from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views.refresh_token_view import RefreshTokenView
from .views.user_registration_viewset import UserRegistrationViewSet
from .views.logout_user_view import LogoutUserView
from .views.user_field_validation_views import check_username_available, check_email_available

app_name = 'core'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationViewSet.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('check_username/', check_username_available, name='check_username'),
    path('check_email/', check_email_available, name='check_email')
]