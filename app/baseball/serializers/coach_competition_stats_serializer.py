from rest_framework import serializers

from ..models.coach_competition_stats import CoachCompetitionStats
from ..models.coach_team_stats import CoachTeamStats

class StatsByTeamField (serializers.RelatedField):
    """Custom relational field for a CoachCompetitionStats' stats_by_team field.
    """
    def to_representation(self, value: CoachTeamStats):
        return str(value.competition_team.team)

class CoachCompetitionStatsSerializer (serializers.ModelSerializer):
    """Serializer for the CoachCompetitionStats model.
    """
    stats_by_team = StatsByTeamField(many=True, read_only=True)

    class Meta:
        model = CoachCompetitionStats
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']