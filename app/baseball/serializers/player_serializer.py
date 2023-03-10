from rest_framework import serializers

from ..models.player import Player

class PlayerSerializer (serializers.ModelSerializer):
    """Serializer for the player model.
    """

    class Meta:
        model = Player
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']