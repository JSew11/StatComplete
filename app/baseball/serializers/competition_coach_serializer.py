from rest_framework import serializers

from ..models.competition_coach import CompetitionCoach
from ..models.team_coach import TeamCoach

class StatsByTeamField (serializers.RelatedField):
    """Custom relational field for a CompetitionCoach's stats_by_team field.
    """
    def to_representation(self, value: TeamCoach):
        return str(value.competition_team.team)

class CompetitionCoachSerializer (serializers.ModelSerializer):
    """Serializer for the CompetitionCoach model.
    """
    stats_by_team = StatsByTeamField(many=True, read_only=True)

    class Meta:
        model = CompetitionCoach
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']