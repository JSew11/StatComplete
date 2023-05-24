from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class LoginUserSerializer (TokenObtainPairSerializer):
    """Serializer to log a user into the system.
    """
    username_field = get_user_model().USERNAME_FIELD