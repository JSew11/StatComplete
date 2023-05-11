from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

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
            'username': 'TestUser',
            'email': 'test.user@email.com',
            'password': 'terriblePassword123'
        }
        response = self.client.post(path='/api/register/', data=user_data, format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)