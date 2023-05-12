from datetime import datetime
from rest_framework import serializers

from ..models.team_player import TeamPlayer
from ..models.player_game_stats import PlayerGameStats
from ..models.player_baserunning_stats import PlayerBaserunningStats
from ..models.player_pitching_stats import PlayerPitchingStats

class StatsByGameField (serializers.RelatedField):
    """Custom relational field for a team player's stats by game.
    """
    def to_representation(self, value: PlayerGameStats):
        return 'Game stats' # TODO: return the opposing team name and game date

class TeamPlayerSerializer (serializers.ModelSerializer):
    """Serializer for the TeamCoach model.
    """
    stats_by_game = StatsByGameField(many=True, read_only=True)

    class Meta:
        model = TeamPlayer
        exclude = ['created', 'updated', 'deleted']
        read_only = ['id']
    
    def create(self, validated_data):
        """Overwritten create method to instantiate stats models when creating
        a new team player model.
        """
        validated_data['joined_team'] = datetime.now()
        validated_data['baserunning_stats'] = PlayerBaserunningStats().save()
        validated_data['pitching_stats'] = PlayerPitchingStats().save()
        # TODO: make new stats models here
        return super().create(validated_data)