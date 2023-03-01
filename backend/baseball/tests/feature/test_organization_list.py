from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from baseball.models.organization import Organization

class TestOrganizationListApi (APITestCase):
    """Tests for endpoints defined in the OrganizationList view.
    """
    fixtures = ['user']

    def setUp(self) -> None:
        """Set up necessary objects for testing.
        """
        Organization.objects.create(
            name = 'Test ORganization',
        )
        Organization.objects.create(
            name = 'Test Organization 2',
        )
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