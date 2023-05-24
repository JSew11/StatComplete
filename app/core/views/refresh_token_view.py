from django.conf import settings
from rest_framework_simplejwt.views import TokenRefreshView

from ..serializers.refresh_token_serializer import RefreshTokenSerializer

class RefreshTokenView(TokenRefreshView):
    """Custom token refresh endpoint to get refresh token from cookies.
    """
    serializer_class = RefreshTokenSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            cookie_max_age = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']
            response.set_cookie('refresh_token', response.data['refresh'], max_age=cookie_max_age, httponly=True, secure=True)
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)