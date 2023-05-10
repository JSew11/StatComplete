from rest_framework import generics, status
from rest_framework.response import Response
from ..serializers.register_serializer import RegisterSerializer
from ..serializers.user_serializer import UserSerializer

class RegisterView(generics.GenericAPIView):
    """View for registering a new user to the system.
    """
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        """Create a new user.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            data = {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "message": "User created successfully",
            },
            status = status.HTTP_201_CREATED
        )