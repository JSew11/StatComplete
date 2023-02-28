from rest_framework import generics, permissions

from ..serializers.user_serializer import UserSerializer

class ManageUserView (generics.RetrieveUpdateAPIView):
    """View to manage the authenticated user.
    """
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve the authenticated user.
        """
        return self.request.user