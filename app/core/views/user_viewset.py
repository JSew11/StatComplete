from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.user import User
from ..serializers.user_serializer import UserSerializer

class UserListView (ListAPIView):
    """Views for the user model.
    """
    serializer_class = UserSerializer
    model = User
    queryset = User.objects.order_by('created')
    permission_classes = [permissions.IsAdminUser]