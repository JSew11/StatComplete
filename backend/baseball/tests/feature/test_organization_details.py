from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from baseball.models.organization import Organization

class TestOrganizationDetailsApi (APITestCase):
    """Tests for endpoints defined in the OrganizationDetailsView.
    """

    def setUp(self) -> None:
        """ Set up necessary objects for testing.
        """
        self.test_organization: Organization = Organization.objects.create(
            name = 'Test Organization',
        )
        self.test_organization_id = self.test_organization.id
        self.client = APIClient()
        return super().setUp()
    
    def test_organization_by_id(self):
        """Test the GET endpoint for getting a organization by its associated uuid.
        """
        response = self.client.get(f'/api/baseball/organizations/{self.test_organization_id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.test_organization.name, response.data.get('name'))

    def test_edit_organization(self):
        """Test the PUT endpoint for editing a organization's info.
        """
        updated_organization_field = {
            'location':'Anywhere, USA',
        }
        response = self.client.put(path=f'/api/baseball/organizations/{self.test_organization_id}/', data=updated_organization_field, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(updated_organization_field.get('location'), response.data.get('location'))
    

    def test_delete_organization(self):
        """Test the DELETE endpoint for deleting a organization by its associated uuid.
        """
        delete_response = self.client.delete(path=f'/api/baseball/organizations/{self.test_organization_id}/')
        self.assertEqual(status.HTTP_204_NO_CONTENT, delete_response.status_code)

        get_response = self.client.get(path=f'/api/baseball/organizations/{self.test_organization_id}/')
        self.assertEqual(status.HTTP_404_NOT_FOUND, get_response.status_code)