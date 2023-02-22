from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from baseball.models.competition import Competition

class TestCompetitionDetailsApi (APITestCase):
    """Tests for endpoints defined in the CompetitionDetailsView.
    """

    def setUp(self) -> None:
        """ Set up necessary objects for testing.
        """
        self.test_competition: Competition = Competition.objects.create(
            name = 'Test Season',
            type = Competition.CompetitionType.SEASON
        )
        self.test_competition_id = self.test_competition.id
        self.client = APIClient()
        return super().setUp()
    
    def test_competition_by_id(self):
        """Test the GET endpoint for getting a competition by its associated uuid.
        """
        response = self.client.get(f'/competitions/{self.test_competition_id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.test_competition.name, response.data.get('name'))
        self.assertEqual(self.test_competition.type, response.data.get('type'))

    def test_edit_competition(self):
        """Test the PUT endpoint for editing a competition's info.
        """
        self.assertEqual(1, 0)

    def test_delete_competition(self):
        """Test the DELETE endpoint for deleting a competition by its associated uuid.
        """
        self.assertEqual(1, 0)