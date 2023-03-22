from rest_framework import serializers

from ..models.game import Game
from ..models.team_box_score import TeamBoxScore

class TeamsField (serializers.RelatedField):
    """Custom relational field for a gem's teams field.
    """
    def to_representation(self, value: TeamBoxScore):
        team = str(value.competition_team.team)
        if value.is_home_team:
            team = team + ' (H)'
        else:
            team = team + ' (A)'
        return team

class GameSerializer (serializers.ModelSerializer):
    """Serializer for the game model.
    """
    teams = TeamsField(many=True, read_only=True)

    class Meta:
        model = Game
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']