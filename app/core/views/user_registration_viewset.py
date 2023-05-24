from django.conf import settings
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework import status, permissions

from ..models.user import User
from ..serializers.register_user_serializer import RegisterUserSerializer

class UserRegistrationViewSet(ListCreateAPIView):
    """Views for creating a new user model.
    """
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()

    def finalize_response(self, request: Request, response: Response, *args, **kwargs):
        if response.data.get('refresh'):
            cookie_max_age = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']
            response.set_cookie('refresh_token', response.data['refresh'], max_age=cookie_max_age, httponly=True, secure=True)
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)
    
    def create(self, request: Request, *args, **kwargs) -> Response:
        """Create a new user.
        """
        serializer: RegisterUserSerializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = TokenObtainPairSerializer.get_token(user)
            access = AccessToken().for_user(user)
            return Response(
                data={
                    'refresh': str(refresh),
                    'access': str(access)
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )