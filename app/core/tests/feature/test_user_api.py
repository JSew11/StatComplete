from rest_framework.test import APITestCase, APIClient
from rest_framework.response import Response
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

class TestUserFieldValidationApi(APITestCase):
    """Test endpoints defined in the user field validation view.
    """
    fixtures = ['user']

    def setUp(self) -> None:
        self.client = APIClient()
        return super().setUp()
    
    def test_check_username_available(self):
        """Test the POST endpoint for checking if a username is available.
        """
        response: Response = self.client.post(path='/api/check_username/', data={}, format='json')
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

        username_data = {
            'username': 'AvailableUsername'
        }
        response: Response = self.client.post(path='/api/check_username/', data=username_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTrue(response.data['username_available'])

        username_data = {
            'username': 'DeveloperAdmin'
        }
        response: Response = self.client.post(path='/api/check_username/', data=username_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertFalse(response.data['username_available'])
    
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