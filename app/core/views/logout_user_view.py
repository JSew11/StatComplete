from rest_framework_simplejwt.views import TokenBlacklistView

from ..serializers.logout_user_serializer import LogoutUserSerializer

class LogoutUserView(TokenBlacklistView):
    """Custom logout endpoint to get refresh token from cookies.
    """
    serializer_class = LogoutUserSerializer