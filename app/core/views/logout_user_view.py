from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenBlacklistView

from ..serializers.logout_user_serializer import LogoutUserSerializer

class LogoutUserView(TokenBlacklistView):
    """Custom logout endpoint to get refresh token from cookies.
    """
    serializer_class = LogoutUserSerializer

    def finalize_response(self, request: Request, response: Response, *args, **kwargs):
        response.delete_cookie('refresh_token')
        return super().finalize_response(request, response, *args, **kwargs)