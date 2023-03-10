from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from baseball.models.coach import Coach

class TestCoachDetailsApi (APITestCase):
    """Tests for endpoints defined in CoachDetails view.
    """
    fixtures = ['user']

    def setUp(self) -> None:
        """Set up necessary objects for testing and log in the appropriate test user(s).
        """
        self.test_coach: Coach = Coach.objects.create(
            first_name = 'Test',
            last_name = 'Coach',
        )
        self.test_coach_id = self.test_coach.id
        self.client = APIClient()
        user = User.objects.get(username='DeveloperAdmin')
        self.client.force_authenticate(user)
        return super().setUp()

    def test_coach_by_id(self):
        """Test the GET endpoint for getting a coach by its associated uuid.
        """
        response = self.client.get(path=f'/api/baseball/coaches/{self.test_coach_id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.test_coach.first_name, response.data.get('first_name'))
        self.assertEqual(self.test_coach.last_name, response.data.get('last_name'))
    
    def test_edit_coach(self):
        """Test the PUT endpoint for editing a coach's info.
        """
        updated_coach_field = {
            'birth_date':'2000-01-01',
        }
        response = self.client.put(path=f'/api/baseball/coaches/{self.test_coach_id}/', data=updated_coach_field, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(updated_coach_field.get('birth_date'), response.data.get('birth_date'))
    
    def test_delete_coach(self):
        """Test the DELETE endpoint for deleting a coach using its associated uuid.
        """
        delete_response = self.client.delete(path=f'/api/baseball/coaches/{self.test_coach_id}/')
        self.assertEqual(status.HTTP_204_NO_CONTENT, delete_response.status_code)

        get_response = self.client.get(path=f'/api/baseball/coaches/{self.test_coach_id}/')
        self.assertEqual(status.HTTP_404_NOT_FOUND, get_response.status_code)