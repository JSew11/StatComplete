from django.test import TestCase

from baseball.models.competition_team import CompetitionTeam

class TestCompetitionTeam (TestCase):
    """Tests for the competition team model.
    """
    fixtures = []

    def setUp(self) -> None:
        return super().setUp()
    
    def test_competition_coach_string(self):
        """Test the overwritten __str__ method for the competition team model.
        """
        self.assertEqual(True, False)