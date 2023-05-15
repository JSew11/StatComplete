from datetime import datetime
from rest_framework import serializers

from ..models.team_player import TeamPlayer
from ..models.game import Game
from ..models.player_game_stats import PlayerGameStats

class StatsByGameField (serializers.RelatedField):
    """Custom relational field for a team player's stats by game.
    """
    def to_representation(self, value: PlayerGameStats):
        game: Game = value.game_box_score.game
        opposing_team = game.get_opposing_team(value.team_player.competition_team)
        return 'Game stats' # TODO: return the opposing team name and game date

class TeamPlayerSerializer (serializers.ModelSerializer):
    """Serializer for the TeamCoach model.
    """
    stats_by_game = StatsByGameField(many=True, read_only=True)

    class Meta:
        model = TeamPlayer
        exclude = ['created', 'updated', 'deleted']
        read_only = ['id']
    