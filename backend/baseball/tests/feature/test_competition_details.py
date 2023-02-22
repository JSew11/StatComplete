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
        updated_competition_field = {
            'start_date':'2023-03-31',
        }
        response = self.client.put(path=f'/competitions/{self.test_competition_id}/', data=updated_competition_field, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(updated_competition_field.get('start_date'), response.data.get('start_date'))
    

    def test_delete_competition(self):
        """Test the DELETE endpoint for deleting a competition by its associated uuid.
        """
        delete_response = self.client.delete(path=f'/competitions/{self.test_competition_id}/')
        self.assertEqual(status.HTTP_204_NO_CONTENT, delete_response.status_code)

        get_response = self.client.get(path=f'/competitions/{self.test_competition_id}/')
        self.assertEqual(status.HTTP_404_NOT_FOUND, get_response.status_code)