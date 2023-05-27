from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from core.models.user import User
from core.models.organization import Organization

class TestOrganizationDetailsApi (APITestCase):
    """Tests for endpoints defined in the OrganizationDetailsView.
    """
    fixtures = ['user', 'organization']

    def setUp(self) -> None:
        """ Set up necessary objects for testing.
        """
        self.test_organization: Organization = Organization.objects.get(name='StatComplete')
        self.client = APIClient()
        user = User.objects.get(email='developer.admin@statcomplete.com')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_organization_by_id(self):
        """Test the GET endpoint for getting a organization by its associated uuid.
        """
        response = self.client.get(f'/api/organizations/{self.test_organization.id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.test_organization.name, response.data.get('name'))

    def test_edit_organization(self):
        """Test the PATCH endpoint for editing a organization's info.
        """
        updated_organization_field = {
            'location':'Anywhere, USA',
        }
        response = self.client.patch(path=f'/api/organizations/{self.test_organization.id}/', data=updated_organization_field, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(updated_organization_field.get('location'), response.data.get('location'))
    

    def test_delete_organization(self):
        """Test the DELETE endpoint for deleting a organization by its associated uuid.
        """
        delete_response = self.client.delete(path=f'/api/organizations/{self.test_organization.id}/')
        self.assertEqual(status.HTTP_204_NO_CONTENT, delete_response.status_code)

        get_response = self.client.get(path=f'/api/organizations/{self.test_organization.id}/')
        self.assertEqual(status.HTTP_404_NOT_FOUND, get_response.status_code)

class TestOrganizationListApi (APITestCase):
    """Tests for endpoints defined in the OrganizationList view.
    """
    fixtures = ['user', 'organization']

    def setUp(self) -> None:
        """Set up necessary objects for testing.
        """
        Organization.objects.get(name='StatComplete')
        Organization.objects.get(name = 'Test Organization 2')
        self.client = APIClient()
        user = User.objects.get(email='developer.admin@statcomplete.com')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_create_organization(self):
        """Test the POST endpoint for creating a organization.
        """
        organization_data = {
            'name' : 'Test Organization Create',
        }
        response = self.client.post('/api/organizations/', data=organization_data, format='json')
        
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(organization_data.get('name'), response.data.get('name'))
        self.assertEqual(organization_data.get('type'), response.data.get('type'))

    def test_organizations_list(self):
        """Test the GET endpoint for getting the list of organizations.
        """
        response = self.client.get('/api/organizations/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data))