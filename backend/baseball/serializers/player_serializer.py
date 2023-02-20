from rest_framework import serializers

from ..models.player import Player
from ..models.player_competition_stats import PlayerCompetitionStats

class StatsByCompetitionField (serializers.RelatedField):
    """Custom relational serializer for a player's stats by competition.
    """
    def to_representation(self, value: PlayerCompetitionStats):
        """Overwritten method that shows how each PlayerCompetitionStats in the stats_by_competition
        will be displayed."""
        return f'{value.competition.name}'
    
class PlayerSerializer (serializers.ModelSerializer):
    """Serializer for the player model.
    """
    stats_by_competition = StatsByCompetitionField(many=True, read_only=True)

    class Meta:
        model = Player
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']