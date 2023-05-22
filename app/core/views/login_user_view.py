from django.conf import settings
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from ..serializers.login_user_serializer import LoginUserSerializer

class LoginUserView (TokenObtainPairView):
    """Custom login endpoint to use email instead of username.
    """
    serializer_class = LoginUserSerializer

    def finalize_response(self, request: Request, response: Response, *args, **kwargs):
        if response.data.get('refresh'):
            cookie_max_age = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']
            response.set_cookie('refresh_token', response.data['refresh'], max_age=cookie_max_age, httponly=True, secure=True)
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)