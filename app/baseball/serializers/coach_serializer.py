from rest_framework import serializers

from ..models.coach import Coach
from ..models.competition_coach import CompetitionCoach

class StatsByCompetitionField (serializers.RelatedField):
    """Custom relational field for a coach's stats by competition.
    """
    def to_representation(self, value: CompetitionCoach):
        """Overwritten method that shows how each CoachCompetitionStats in the stats_by_competition
        will be displayed."""
        return f'{value.competition.name}'

class CoachSerializer (serializers.ModelSerializer):
    """Serializer for the coach model.
    """
    stats_by_competition = StatsByCompetitionField(many=True, read_only=True)

    class Meta:
        model = Coach
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']