from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from baseball.models.coach import Coach

class TestCoachListApi (APITestCase):
    """Tests for endpoints defined in CoachList view.
    """

    def setUp(self):
        """Set up necessary objects for testing.
        """
        Coach.objects.create(
            first_name = 'Test',
            last_name = 'Coach',
        )
        Coach.objects.create(
            first_name = 'Another',
            last_name = 'Coach',
        )
        self.client = APIClient()
        return super().setUp()

    def test_create_coach(self):
        """Test the POST endpoint for creating a coach.
        """
        coach_data = {
            'first_name' : 'TEST',
            'last_name' : 'COACH',
        }
        response = self.client.post(path='/coaches/', data=coach_data, format='json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(coach_data.get('first_name'), response.data.get('first_name'))
        self.assertEqual(coach_data.get('last_name'), response.data.get('last_name'))
    
    def test_coaches_list(self):
        """Test the GET endpoint for getting the list of coaches.
        """
        response = self.client.get(path='/coaches/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data))