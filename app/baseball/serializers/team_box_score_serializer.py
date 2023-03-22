from rest_framework import serializers

from ..models.team_box_score import TeamBoxScore
from ..models.player_game_stats import PlayerGameStats

class LineupField (serializers.RelatedField):
    """Custom relational field for a team box score's lineup.
    """
    def to_representation(self, value: PlayerGameStats):
        return f'{value.team_player}'


class TeamBoxScoreSerializer (serializers.ModelField):
    """Serializer for the team box score model.
    """
    lineup = LineupField(many=True, read_only=True)

    class Meta:
        model = TeamBoxScore
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']