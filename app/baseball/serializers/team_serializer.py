from rest_framework import serializers

from ..models.team import Team
from ..models.competition_team import CompetitionTeam

class CompetitionTeamsField (serializers.RelatedField):
    """Custom relational field for a team's competition teams.
    """
    def to_representation(self, value: CompetitionTeam):
        """Overwritten method that shows how each CompetitionTeam in the competition_teams
        will be displayed."""
        return f'{value.competition.name}'

class TeamSerializer (serializers.ModelSerializer):
    """Serializer for the team model.
    """
    competitions = CompetitionTeamsField(many=True, read_only=True)

    class Meta:
        model = Team
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']