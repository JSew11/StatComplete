from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from baseball.models.organization import Organization
from baseball.models.competition import Competition

class TestOrganizationDetailsApi (APITestCase):
    """Tests for endpoints defined in the OrganizationDetailsView.
    """
    fixtures = ['user', 'organization']

    def setUp(self) -> None:
        """ Set up necessary objects for testing.
        """
        self.test_organization: Organization = Organization.objects.get(name='Test Organization')
        self.client = APIClient()
        user = User.objects.get(username='DeveloperAdmin')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_organization_by_id(self):
        """Test the GET endpoint for getting a organization by its associated uuid.
        """
        response = self.client.get(f'/api/baseball/organizations/{self.test_organization.id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.test_organization.name, response.data.get('name'))

    def test_edit_organization(self):
        """Test the PUT endpoint for editing a organization's info.
        """
        updated_organization_field = {
            'location':'Anywhere, USA',
        }
        response = self.client.put(path=f'/api/baseball/organizations/{self.test_organization.id}/', data=updated_organization_field, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(updated_organization_field.get('location'), response.data.get('location'))
    

    def test_delete_organization(self):
        """Test the DELETE endpoint for deleting a organization by its associated uuid.
        """
        delete_response = self.client.delete(path=f'/api/baseball/organizations/{self.test_organization.id}/')
        self.assertEqual(status.HTTP_204_NO_CONTENT, delete_response.status_code)

        get_response = self.client.get(path=f'/api/baseball/organizations/{self.test_organization.id}/')
        self.assertEqual(status.HTTP_404_NOT_FOUND, get_response.status_code)

class TestOrganizationListApi (APITestCase):
    """Tests for endpoints defined in the OrganizationList view.
    """
    fixtures = ['user', 'organization']

    def setUp(self) -> None:
        """Set up necessary objects for testing.
        """
        Organization.objects.get(name='Test Organization')
        Organization.objects.get(name = 'Test Organization 2')
        self.client = APIClient()
        user = User.objects.get(username='DeveloperAdmin')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_create_organization(self):
        """Test the POST endpoint for creating a organization.
        """
        organization_data = {
            'name' : 'Test Organization Create',
        }
        response = self.client.post('/api/baseball/organizations/', data=organization_data, format='json')
        
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(organization_data.get('name'), response.data.get('name'))
        self.assertEqual(organization_data.get('type'), response.data.get('type'))

    def test_organizations_list(self):
        """Test the GET endpoint for getting the list of organizations.
        """
        response = self.client.get('/api/baseball/organizations/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data))

class TestOrganizationCompetitionDetailsApi (APITestCase):
    """Tests for endpoints defined in the CompetitionDetails view.
    """
    fixtures = ['user', 'organization', 'competition']

    def setUp(self) -> None:
        """ Set up necessary objects for testing.
        """
        self.test_organization: Organization = Organization.objects.get(name='Test Organization')
        self.test_competition: Competition = Competition.objects.get(name='Test Season')
        self.client = APIClient()
        user = User.objects.get(username='DeveloperAdmin')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_competition_by_id(self):
        """Test the GET endpoint for getting a competition by its associated uuid.
        """
        response = self.client.get(f'/api/baseball/organizations/{self.test_organization.id}/competitions/{self.test_competition.id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.test_competition.name, response.data.get('name'))
        self.assertEqual(self.test_competition.type, response.data.get('type'))

    def test_edit_competition(self):
        """Test the PUT endpoint for editing a competition's info.
        """
        updated_competition_data = {
            'start_date':'2023-03-31',
        }
        response = self.client.put(path=f'/api/baseball/organizations/{self.test_organization.id}/competitions/{self.test_competition.id}/', data=updated_competition_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(updated_competition_data.get('start_date'), response.data.get('start_date'))
    

    def test_delete_competition(self):
        """Test the DELETE endpoint for deleting a competition by its associated uuid.
        """
        delete_response = self.client.delete(path=f'/api/baseball/organizations/{self.test_organization.id}/competitions/{self.test_competition.id}/')
        self.assertEqual(status.HTTP_204_NO_CONTENT, delete_response.status_code)

        get_response = self.client.get(path=f'/api/baseball/organizations/{self.test_organization.id}/competitions/{self.test_competition.id}/')
        self.assertEqual(status.HTTP_404_NOT_FOUND, get_response.status_code)

class TestOrganizationCompetitionListApi (APITestCase):
    """Tests for endpoints defined in the CompetitionList view.
    """
    fixtures = ['user', 'organization', 'competition']

    def setUp(self) -> None:
        """Set up necessary objects for testing.
        """
        self.test_organization: Organization = Organization.objects.get(name='Test Organization')
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
        response = self.client.post(f'/api/baseball/organizations/{self.test_organization.id}/competitions/', data=competition_data, format='json')
        
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(competition_data.get('name'), response.data.get('name'))
        self.assertEqual(competition_data.get('type'), response.data.get('type'))

    def test_competitions_list(self):
        """Test the GET endpoint for getting the list of competitions.
        """
        response = self.client.get(f'/api/baseball/organizations/{self.test_organization.id}/competitions/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data))