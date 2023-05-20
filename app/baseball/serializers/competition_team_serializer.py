from rest_framework import serializers

from ..models.competition_team import CompetitionTeam

class CompetitionTeamSerializer (serializers.ModelSerializer):
    """Serializer for the competition team model.
    """
    coaching_staff = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    roster = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    games = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CompetitionTeam
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']