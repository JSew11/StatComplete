from rest_framework_simplejwt.views import TokenObtainPairView

from ..serializers.login_user_serializer import LoginUserSerializer

class LoginUserView (TokenObtainPairView):
    """Custom login endpoint to use email instead of username.
    """
    serializer_class = LoginUserSerializer