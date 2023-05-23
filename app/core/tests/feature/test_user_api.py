from rest_framework.test import APITestCase, APIClient
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from http.cookies import SimpleCookie

from core.models.user import User

class TestUserRegistrationApi(APITestCase):
    """Tests for endpoints defined in the registration view.
    """
    def setUp(self) -> None:
        """Set up necessary objects for testing.
        """
        self.client = APIClient()
        return super().setUp()
    
    def test_register_user(self):
        """Test the POST endpoint for registering a new user.
        """
        user_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test.user@email.com',
            'password': 'terriblePassword123'
        }
        response = self.client.post(path='/api/register/', data=user_data, format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

class TestRefreshTokenApi(APITestCase):
    """Test the refresh_token endpoint.
    """
    fixtures = ['user']

    def setUp(self) -> None:
        self.client = APIClient()
        self.test_user = User.objects.get(email='developer.admin@statcomplete.com')
        self.client.force_authenticate(self.test_user)
        token = RefreshToken.for_user(self.test_user)
        self.client.cookies = SimpleCookie({'refresh_token': str(token)})
        return super().setUp()
    
    def test_refresh_token(self):
        """Test the POST endpoint for getting a new access token.
        """
        response: Response = self.client.post(path='/api/login/refresh/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertNotEqual('', response.data.get('access'))

class TestLogoutApi(APITestCase):
    """Test the logout endpoint.
    """
    fixtures = ['user']

    def setUp(self) -> None:
        self.client: APIClient = APIClient()
        self.test_user = User.objects.get(email='developer.admin@statcomplete.com')
        self.client.force_authenticate(self.test_user)
        token = RefreshToken.for_user(self.test_user)
        self.client.cookies = SimpleCookie({'refresh_token': str(token)})
        return super().setUp()
    
    def test_logout(self):
        """Test the POST endpoint for logging a user out.
        """
        response: Response = self.client.post('/api/logout/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

class TestUserFieldValidationApi(APITestCase):
    """Test endpoints defined in the user field validation view.
    """
    fixtures = ['user']

    def setUp(self) -> None:
        self.client = APIClient()
        return super().setUp()
    
    def test_check_email_available(self):
        """Test the POST endpoint for checking if a email is available.
        """
        response: Response = self.client.post(path='/api/check_email/', data={}, format='json')
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

        email_data = {
            'email': 'AvailableEmail'
        }
        response: Response = self.client.post(path='/api/check_email/', data=email_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTrue(response.data['email_available'])

        email_data = {
            'email': 'developer.admin@statcomplete.com'
        }
        response: Response = self.client.post(path='/api/check_email/', data=email_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertFalse(response.data['email_available'])

class TestUserListView(APITestCase):
    """Test the user list endpoint.
    """
    fixtures = ['user']

    def setUp(self) -> None:
        self.client: APIClient = APIClient()
        return super().setUp()
    
    def test_users_list_endpoint(self):
        """Test the GET endpoint for getting a list of users in the system.
        """
        # test as unauthenticated user
        response: Response = self.client.get(path='/api/users/')
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

        # test as non-admin user
        regular_user = User.objects.get(email='test.user@email.com')
        self.client.force_authenticate(regular_user)
        response: Response = self.client.get(path='/api/users/')
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

        # test as admin user
        admin_user = User.objects.get(email='developer.admin@statcomplete.com')
        self.client.force_authenticate(admin_user)
        response: Response = self.client.get(path='/api/users/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

class TestUserViewSet(APITestCase):
    """Test the user viewset endpoint.
    """
    fixtures = ['user']

    def setUp(self) -> None:
        self.client: APIClient = APIClient()
        return super().setUp()

    def test_retrieve_user_endpoint(self):
        """Test the GET endpoint for retrieving a user by its associated uuid.
        """
        regular_user: User = User.objects.get(email='test.user@email.com')
        admin_user: User = User.objects.get(email='developer.admin@statcomplete.com')

        self.client.force_authenticate(regular_user)
        # as the test user test accessing the test user with its uuid (should receive 200)
        response: Response = self.client.get(path=f'/api/users/{regular_user.id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(regular_user.email, response.data['email'])

        # as the test user test accessing the admin user with its uuid (should receive 403)
        response: Response = self.client.get(path=f'/api/users/{admin_user.id}/')
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

        self.client.force_authenticate(admin_user)
        # as the admin user test accessing the test user with its uuid (should receive 200)
        response: Response = self.client.get(path=f'/api/users/{admin_user.id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(admin_user.email, response.data['email'])

        # as the admin user test accessing the admin user with its uuid (should receive 200)
        response: Response = self.client.get(path=f'/api/users/{regular_user.id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(regular_user.email, response.data['email'])