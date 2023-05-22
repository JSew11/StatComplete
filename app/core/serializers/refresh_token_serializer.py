from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import InvalidToken

class RefreshTokenSerializer(TokenRefreshSerializer):
    """Custom token refresh serializer to get refresh token from cookies.
    """
    refresh = None

    def validate(self, attrs):
        attrs['refresh'] = self.context['request'].COOKIES.get('refresh_token')
        if attrs['refresh']:
            return super().validate(attrs)
        raise InvalidToken('No valid token found in cookie \'refresh_token\'.')