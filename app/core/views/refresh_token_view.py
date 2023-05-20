from rest_framework_simplejwt.views import TokenRefreshView

from ..serializers.refresh_token_serializer import RefreshTokenSerializer

class RefreshTokenView(TokenRefreshView):
    """Custom token refresh endpoint to get refresh token from cookies.
    """
    serializer_class = RefreshTokenSerializer