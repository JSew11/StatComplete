from rest_framework import serializers

from ..models.user import User

class RegisterUserSerializer(serializers.ModelSerializer):
    """Serializer to register a new user.
    """
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'middle_name', 'last_name', 'suffix', 'email')
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data: dict) -> User:
        """Method for creating the new user based on the given data.
        """
        user_data = {
            'username': validated_data.pop('username'),
            'password': validated_data.pop('password'),
            'first_name': validated_data.pop('first_name'),
            'last_name': validated_data.pop('last_name'),
            'email': validated_data.pop('email'),
        }

        if middle_name := validated_data.pop('middle_name', None):
            user_data['middle_name'] = middle_name


        if suffix := validated_data.pop('suffix', None):
            user_data['suffix'] = suffix

        user: User = User.objects.create_user(
            **user_data
        )
        return user