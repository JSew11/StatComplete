from rest_framework import serializers

from ..models.competition import Competition
from ..models.competition_team import CompetitionTeam
    
class TeamsField (serializers.RelatedField):
    """Custom relational field for a competition's teams.
    """
    def to_representation(self, value: CompetitionTeam):
        return f'{value.team.location} {value.team.name}'

class CompetitionSerializer (serializers.ModelSerializer):
    """Serializer for the competition model.
    """
    teams = TeamsField(many=True, read_only=True)

    class Meta:
        model = Competition
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']