from rest_framework import serializers

from ..models.coach import Coach
from ..models.coach_stats import CoachStats

class StatsByTeamField(serializers.RelatedField):
    """Custom relational serializer for a Coach's stats by team.
    """
    def to_representation(self, value: CoachStats):
        """Overwritten method that shows how each CoachStats in the stats_by_team
        will be displayed."""
        if value.role:
            return f'Associated Team Name {value.role}'
        else:
            return 'Associated Team Name'

class CoachSerializer(serializers.ModelSerializer):
    """Serializer for the Coach model.
    """
    stats_by_team = StatsByTeamField(many=True, read_only=True)

    class Meta:
        model = Coach
        fields = '__all__'