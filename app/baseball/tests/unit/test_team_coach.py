from django.test import TestCase

from baseball.models.team_coach import TeamCoach

class TestTeamCoachModel (TestCase):
    """Tests for the team coach model.
    """
    fixtures = ['organization', 'competition', 'team', 'competition_team', 'coach', 'team_coach']

    def setUp(self) -> None:
        self.test_team_coach = TeamCoach.objects.get(
            coach__first_name='Test',
            coach__last_name='Coach'
        )
        return super().setUp()
    
    def test_team_coach_string(self):
        """Test the overwritten __str__ method for the team coach model.
        """
        coach_string_representation = str(self.test_team_coach.coach)+f' #{self.test_team_coach.jersey_number}'
        self.assertEqual(coach_string_representation, str(self.test_team_coach))