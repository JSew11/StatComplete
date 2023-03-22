from rest_framework import serializers

from ..models.coach import Coach
from ..models.team_coach import TeamCoach

class StatsByTeamField (serializers.RelatedField):
    """Custom relational field for a coach's stats by team.
    """
    def to_representation(self, value: TeamCoach):
        return str(value.competition_team)

class CoachSerializer (serializers.ModelSerializer):
    """Serializer for the coach model.
    """
    
    class Meta:
        model = Coach
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']