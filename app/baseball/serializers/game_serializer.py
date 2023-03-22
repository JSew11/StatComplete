from rest_framework import serializers

from ..models.game import Game

class GameSerializer (serializers.ModelSerializer):
    """Serializer for the game model.
    """

    class Meta:
        model = Game
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']