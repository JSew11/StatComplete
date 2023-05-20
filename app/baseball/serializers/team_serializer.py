from rest_framework import serializers

from ..models.team import Team
class TeamSerializer (serializers.ModelSerializer):
    """Serializer for the team model.
    """
    competition_teams = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Team
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']