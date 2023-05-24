from django.urls import path, include

from ..views.login_user_view import LoginUserView
from ..views.refresh_token_view import RefreshTokenView
from ..views.user_registration_viewset import UserRegistrationViewSet
from ..views.logout_user_view import LogoutUserView
from ..views.user_field_validation_views import check_email_available
from ..views.user_viewset import UserListView, UserViewSet

app_name = 'core'

current_user_view = UserViewSet.as_view({
    'get': 'current_user',
})

user_viewset = UserViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
})

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('login/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationViewSet.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('check_email/', check_email_available, name='check_email'),
    path('users/', UserListView.as_view(), name='users_list'),
    path('users/me/', current_user_view, name='current_user'),
    path('users/<uuid:user_id>/', user_viewset, name='user_details'),
    path('organizations/', include('core.urls.organization_urls')),
]