from rest_framework import serializers

from ..models.competition import Competition
from ..models.coach_competition_stats import CoachCompetitionStats
from ..models.player_competition_stats import PlayerCompetitionStats
    
class CompetitionCoachField (serializers.RelatedField):
    """Custom relational field for a competition's coaches.
    """
    def to_representation(self, value: CoachCompetitionStats):
        return f'{value.coach.first_name} {value.coach.last_name}'

class CompetitionPlayerField (serializers.RelatedField):
    """Custom relational field for a competition's players.
    """
    def to_representation(self, value: PlayerCompetitionStats):
        return f'{value.player.first_name} {value.player.last_name}'

class CompetitionSerializer (serializers.ModelSerializer):
    """Serializer for the competition model.
    """
    coaches = CompetitionCoachField(many=True, read_only=True)
    players = CompetitionPlayerField(many=True, read_only=True)

    class Meta:
        model = Competition
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']