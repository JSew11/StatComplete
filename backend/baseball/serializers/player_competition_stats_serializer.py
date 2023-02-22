from rest_framework import serializers

from ..models.player_competition_stats import PlayerCompetitionStats

class PlayerCompetitionStatsSerializer (serializers.ModelSerializer):
    """Serializer for the PlayerCompetitionStats model.
    """

    class Meta:
        model = PlayerCompetitionStats
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']