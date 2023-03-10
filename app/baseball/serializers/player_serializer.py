from rest_framework import serializers

from ..models.player import Player
from ..models.team_player import TeamPlayer

class StatsByTeamField (serializers.RelatedField):
    """Custom relational field for a player's stats by team.
    """
    def to_representation(self, value: TeamPlayer):
        return str(value.competition_team)

class PlayerSerializer (serializers.ModelSerializer):
    """Serializer for the player model.
    """

    class Meta:
        model = Player
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']