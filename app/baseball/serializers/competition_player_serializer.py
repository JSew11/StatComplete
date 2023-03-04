from rest_framework import serializers

from ..models.competition_player import CompetitionPlayer

class CompetitionPlayerSerializer (serializers.ModelSerializer):
    """Serializer for the CompetitionPlayer model.
    """

    class Meta:
        model = CompetitionPlayer
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']