from rest_framework import generics
from rest_framework.response import Response
from knox.models import AuthToken

from ..serializers.user_serializer import UserSerializer

class RegisterUserView (generics.GenericAPIView):
    """Create user API view.
    """
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """Registers a new user and returns the new user and their auth token.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })