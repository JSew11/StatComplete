from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework import status

from ..models.user import User
from ..serializers.register_user_serializer import RegisterUserSerializer

class UserRegistrationViewSet(ListCreateAPIView):
    """Views for creating a new user model.
    """
    queryset = User.objects.all()

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