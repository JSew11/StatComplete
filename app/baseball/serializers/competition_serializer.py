from rest_framework import serializers

from ..models.competition import Competition

class CompetitionSerializer (serializers.ModelSerializer):
    """Serializer for the competition model.
    """
    teams = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    games = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Competition
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']