from rest_framework import serializers

from ..models.player import Player

class PlayerSerializer (serializers.ModelSerializer):
    """Serializer for the player model.
    """
    stats_by_team = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Player
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']