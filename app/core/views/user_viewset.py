from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.user import User
from ..serializers.user_serializer import UserSerializer

class UserListView (ListAPIView):
    """List view for the user model.
    """
    serializer_class = UserSerializer
    model = User
    queryset = User.objects.order_by('created')
    permission_classes = [permissions.IsAdminUser]

class UserViewSet (ModelViewSet):
    """Viewset for the user model. Supports viewing a single user and updating a
    single user.
    """
    serializer_class = UserSerializer

    def retrieve(self, request: Request, user_id: str, *args, **kwargs) -> Response:
        """Get the details of the user with the given user_id.
        """
        request_user: User = request.user
        user_to_return = User.objects.get(id=user_id)
        if request_user.has_perm('core.view_user') or request_user.id == user_to_return.id:
            serializer = UserSerializer(user_to_return)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            data={
                'message': 'You do not have access to this object.',
            },
            status=status.HTTP_403_FORBIDDEN
        )