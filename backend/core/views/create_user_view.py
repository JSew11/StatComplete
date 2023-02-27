from rest_framework import generics

from ..serializers.user_serializer import UserSerializer

class CreateUserView (generics.CreateAPIView):
    """Create user API view.
    """
    serializer_class = UserSerializer