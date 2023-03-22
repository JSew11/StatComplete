from rest_framework import serializers

from ..models.competition_team import CompetitionTeam
from ..models.team_coach import TeamCoach
from ..models.team_player import TeamPlayer
from ..models.team_box_score import TeamBoxScore

class CoachingStaffField (serializers.RelatedField):
    """Custom relational field for the competition team's coaching staff.
    """
    def to_representation(self, value: TeamCoach):
        return str(value)
    
class RosterField (serializers.RelatedField):
    """Custom relational field for the competition team's roster.
    """
    def to_representation(self, value: TeamPlayer):
        return str(value)

class GamesField (serializers.RelatedField):
    """Custom relational field for the competition team's games.
    """
    def to_representation(self, value: TeamBoxScore):
        return f'' # TODO: edit this based on the game status and opposing team

class CompetitionTeamSerializer (serializers.ModelSerializer):
    """Serializer for the competition team model.
    """
    coaching_staff = CoachingStaffField(many=True, read_only=True)
    roster = RosterField(many=True, read_only=True)

    class Meta:
        model = CompetitionTeam
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']