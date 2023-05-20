from rest_framework import serializers

from ..models.player import Player
from ..models.team_player import TeamPlayer

class StatsByTeamField (serializers.RelatedField):
    """Custom relational field for a player's stats by team.
    """
    def to_representation(self, value: TeamPlayer):
        if value:
            return str(value.competition_team)
        return

class PlayerSerializer (serializers.ModelSerializer):
    """Serializer for the player model.
    """
    stats_by_team = StatsByTeamField(many=True, read_only=True)

    class Meta:
        model = Player
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']