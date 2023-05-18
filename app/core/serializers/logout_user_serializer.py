from rest_framework_simplejwt.serializers import TokenBlacklistSerializer
from rest_framework_simplejwt.exceptions import InvalidToken

class LogoutUserSerializer(TokenBlacklistSerializer):
    """Custom logout serializer to get refresh token from cookies.
    """
    refresh = None
    def validate(self, attrs):
        attrs['refresh'] = self.context['request'].COOKIES.get('refresh')
        if attrs['refresh']:
            return super().validate(attrs)
        raise InvalidToken('No valid token found in cookie \'refresh\'.')