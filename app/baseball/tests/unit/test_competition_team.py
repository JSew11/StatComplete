from django.test import TestCase

from baseball.models.competition import Competition
from baseball.models.team import Team
from baseball.models.competition_team import CompetitionTeam

class TestCompetitionTeam (TestCase):
    """Tests for the competition team model.
    """
    fixtures = ['organization', 'competition', 'team', 'competition_team']

    def setUp(self) -> None:
        self.test_competition: Competition = Competition.objects.get(name='Test Season')
        self.test_team: Team = Team.objects.get(location='Test', name='Team')
        self.test_competition_team: CompetitionTeam = CompetitionTeam.objects.get(competition=self.test_competition.id, team=self.test_team.id)
        return super().setUp()
    
    def test_competition_coach_string(self):
        """Test the overwritten __str__ method for the competition team model.
        """
        competition_team_string = f'{self.test_competition} - {self.test_team}'
        self.assertEqual(str(self.test_competition_team), competition_team_string)