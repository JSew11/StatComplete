from rest_framework import serializers

from ..models.team_player import TeamPlayer

class TeamPlayerSerializer (serializers.ModelSerializer):
    """Serializer for the TeamCoach model.
    """
    stats_by_game = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = TeamPlayer
        exclude = ['created', 'updated', 'deleted']
        read_only = ['id']
    