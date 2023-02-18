from rest_framework import serializers

from ..models.coach import Coach
from ..models.coach_competition_stats import CoachCompetitionStats

class StatsByCompetitionField(serializers.RelatedField):
    """Custom relational serializer for a Coach's stats by competition.
    """
    def to_representation(self, value: CoachCompetitionStats):
        """Overwritten method that shows how each CoachCompetitionStats in the stats_by_team
        will be displayed."""
        return f'Associated Competition Name'

class CoachSerializer(serializers.ModelSerializer):
    """Serializer for the Coach model.
    """
    stats_by_team = StatsByCompetitionField(many=True, read_only=True)

    class Meta:
        model = Coach
        fields = '__all__'