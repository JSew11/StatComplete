from rest_framework import serializers

from ..models.user import User

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user model.
    """

    class Meta:
        model = User
        exclude = ['created', 'updated', 'deleted', 'password']
        read_only_fields = ['id']