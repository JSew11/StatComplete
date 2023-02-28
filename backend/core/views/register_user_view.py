from rest_framework import generics

from ..serializers.user_serializer import UserSerializer

class RegisterUserView (generics.CreateAPIView):
    """Create user API view.
    """
    serializer_class = UserSerializer