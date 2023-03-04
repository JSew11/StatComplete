from rest_framework import serializers

from ..models.competition import Competition
from ..models.competition_coach import CompetitionCoach
from ..models.competition_player import CompetitionPlayer
from ..models.competition_team import CompetitionTeam
    
class CompetitionCoachField (serializers.RelatedField):
    """Custom relational field for a competition's coaches.
    """
    def to_representation(self, value: CompetitionCoach):
        return f'{value.coach.first_name} {value.coach.last_name}'

class CompetitionPlayerField (serializers.RelatedField):
    """Custom relational field for a competition's players.
    """
    def to_representation(self, value: CompetitionPlayer):
        return f'{value.player.first_name} {value.player.last_name}'

class CompetitionTeamsField (serializers.RelatedField):
    """Custom relational field for a competition's teams.
    """
    def to_representation(self, value: CompetitionTeam):
        return f'{value.team.location} {value.team.name}'

class CompetitionSerializer (serializers.ModelSerializer):
    """Serializer for the competition model.
    """
    coaches = CompetitionCoachField(many=True, read_only=True)
    players = CompetitionPlayerField(many=True, read_only=True)

    class Meta:
        model = Competition
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']