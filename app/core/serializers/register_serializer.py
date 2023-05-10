from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    """Serializer to register a new user.
    """
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data) -> User:
        """Method for creating the new user based on the given data.
        """
        user: User = User.objects.create_user(
            validated_data['username'],
            password = validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user