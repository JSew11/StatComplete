from django.urls import path
from knox import views as knox_views

from core.views.register_user_view import RegisterUserView
from core.views.login_view import LoginView
from core.views.manage_user_view import ManageUserView

app_name = 'core'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='create'),
    path('profile/', ManageUserView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]