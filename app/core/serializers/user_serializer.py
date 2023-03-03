from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer (serializers.ModelSerializer):
    """Serializer for the user model.
    """

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)