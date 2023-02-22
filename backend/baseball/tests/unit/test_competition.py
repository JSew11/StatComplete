from django.test import TestCase

from baseball.models.competition import Competition

class TestCompetitionModel (TestCase):
    """Tests for the competition model.
    """

    def setUp(self) -> None:
        self.test_competition = Competition.objects.create(
            name = 'Test Competition',
            type = Competition.CompetitionType.SEASON
        )
        return super().setUp()
    
    def test_competition_string(self):
        """Test the overwritten __str__ method for the competition model.
        """
        competition_string_representation = self.test_competition.name
        self.assertEqual(competition_string_representation, str(self.test_competition))