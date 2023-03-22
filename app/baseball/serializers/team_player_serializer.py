from rest_framework import serializers

from ..models.team_player import TeamPlayer

class TeamPlayerSerializer (serializers.ModelSerializer):
    """Serializer for the TeamCoach model.
    """

    class Meta:
        model = TeamPlayer
        exclude = ['created', 'updated', 'deleted']
        read_only = ['id']