from django.test import TestCase

from baseball.models.coach import Coach
from baseball.models.coach_competition_stats import CoachCompetitionStats

class TestCoachModel (TestCase):
    """Tests for the coach model.
    """

    def setUp(self) -> None:
        self.test_coach = Coach.objects.create(
            first_name = 'Test',
            last_name = 'Coach'
        )
        self.test_coach_stats = CoachCompetitionStats.objects.create(
            coach = self.test_coach,
            jersey_number = 1,
            role = CoachCompetitionStats.ROLES['MANAGER']
        )
        return super().setUp()
    
    def test_coach_string(self):
        """Test the overwritten __str__ method for the coach model.
        """
        coach_string_representation = 'Coach '+self.test_coach.first_name+' '+self.test_coach.last_name
        self.assertEqual(coach_string_representation, str(self.test_coach))