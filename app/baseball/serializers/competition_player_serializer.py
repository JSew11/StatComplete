from rest_framework import serializers

from ..models.competition_player import CompetitionPlayer
from ..models.team_player import TeamPlayer

class StatsByTeamField (serializers.RelatedField):
    """Custom relational field for a CompetitionPlayer's stats_by_team field.
    """
    def to_representation(self, value: TeamPlayer):
        return str(value.competition_team.team)

class CompetitionPlayerSerializer (serializers.ModelSerializer):
    """Serializer for the CompetitionPlayer model.
    """
    stats_by_team = StatsByTeamField(many=True, read_only=True)

    class Meta:
        model = CompetitionPlayer
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']