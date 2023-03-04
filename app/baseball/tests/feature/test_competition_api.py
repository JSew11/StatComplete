from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from baseball.models.competition import Competition

class TestCompetitionDetailsApi (APITestCase):
    """Tests for endpoints defined in the CompetitionDetailsView.
    """
    fixtures = ['user', 'competition']

    def setUp(self) -> None:
        """ Set up necessary objects for testing.
        """
        self.test_competition: Competition = Competition.objects.get(name='Test Season')
        self.test_competition_id = self.test_competition.id
        self.client = APIClient()
        user = User.objects.get(username='DeveloperAdmin')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_competition_by_id(self):
        """Test the GET endpoint for getting a competition by its associated uuid.
        """
        response = self.client.get(f'/api/baseball/competitions/{self.test_competition_id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.test_competition.name, response.data.get('name'))
        self.assertEqual(self.test_competition.type, response.data.get('type'))

    def test_edit_competition(self):
        """Test the PUT endpoint for editing a competition's info.
        """
        updated_competition_field = {
            'start_date':'2023-03-31',
        }
        response = self.client.put(path=f'/api/baseball/competitions/{self.test_competition_id}/', data=updated_competition_field, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(updated_competition_field.get('start_date'), response.data.get('start_date'))
    

    def test_delete_competition(self):
        """Test the DELETE endpoint for deleting a competition by its associated uuid.
        """
        delete_response = self.client.delete(path=f'/api/baseball/competitions/{self.test_competition_id}/')
        self.assertEqual(status.HTTP_204_NO_CONTENT, delete_response.status_code)

        get_response = self.client.get(path=f'/api/baseball/competitions/{self.test_competition_id}/')
        self.assertEqual(status.HTTP_404_NOT_FOUND, get_response.status_code)

class TestCompetitionListApi (APITestCase):
    """Tests for endpoints defined in the CompetitionList view.
    """
    fixtures = ['user', 'competition']

    def setUp(self) -> None:
        """Set up necessary objects for testing.
        """
        self.client = APIClient()
        user = User.objects.get(username='DeveloperAdmin')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_create_competition(self):
        """Test the POST endpoint for creating a competition.
        """
        competition_data = {
            'name' : 'Test Season',
            'type' : Competition.CompetitionType.SEASON
        }
        response = self.client.post('/api/baseball/competitions/', data=competition_data, format='json')
        
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(competition_data.get('name'), response.data.get('name'))
        self.assertEqual(competition_data.get('type'), response.data.get('type'))

    def test_competitions_list(self):
        """Test the GET endpoint for getting the list of competitions.
        """
        response = self.client.get('/api/baseball/competitions/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data))