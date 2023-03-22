from rest_framework import serializers

from ..models.team_box_score import TeamBoxScore

class TeamBoxScoreSerializer (serializers.ModelField):
    """Serializer for the team box score model.
    """

    class Meta:
        model = TeamBoxScore
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']