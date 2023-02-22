from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from baseball.models.competition import Competition

class TestCompetitionListApi (APITestCase):
    """Tests for endpoints defined in the CompetitionList view.
    """

    def setUp(self) -> None:
        Competition.objects.create(
            name = 'Test Season',
            type = Competition.CompetitionType.SEASON
        )
        Competition.objects.create(
            name = 'Test Tournament',
            type = Competition.CompetitionType.TOURNAMENT
        )
        self.client = APIClient()
        return super().setUp()
    
    def test_create_competition(self):
        """Test the POST endpoint for creating a competition.
        """
        competition_data = {
            'name' : 'Test Season',
            'type' : Competition.CompetitionType.SEASON
        }
        response = self.client.post('/competitions/', data=competition_data, format='json')
        
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(competition_data.get('name'), response.data.get('name'))
        self.assertEqual(competition_data.get('type'), response.data.get('type'))

    def test_competitions_list(self):
        """Test the GET endpoint for getting the list of competitions.
        """
        response = self.client.get('/competitions/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data))