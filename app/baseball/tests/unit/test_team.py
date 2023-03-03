from django.test import TestCase

from baseball.models.team import Team

class TestTeamModel (TestCase):
    """Tests for the team model.
    """

    def setUp(self) -> None:
        self.test_team = Team.objects.create(
            name = 'Team',
            location = 'Test'
        )
        return super().setUp()
    
    def test_team_string(self):
        """Test the overwritten __str__ method for the team model.
        """
        team_string_representation = f'{self.test_team.location} {self.test_team.name}'
        self.assertEqual(team_string_representation, str(self.test_team))