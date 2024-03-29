from django.test import TestCase

from core.models.organization import Organization

class TestOrganizationModel (TestCase):
    """Tests for the organization model.
    """
    fixtures = ['organization']

    def setUp(self) -> None:
        self.test_organization = Organization.objects.get(name='StatComplete')
        return super().setUp()
    
    def test_organization_string(self):
        """Test the overwritten __str__ method for the organization model.
        """
        organization_string_representation = self.test_organization.name
        self.assertEqual(organization_string_representation, str(self.test_organization))