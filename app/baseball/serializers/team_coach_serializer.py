from datetime import datetime
from rest_framework import serializers

from ..models.team_coach import TeamCoach

class TeamCoachSerializer (serializers.ModelSerializer):
    """Serializer for the TeamCoach model.
    """

    class Meta:
        model = TeamCoach
        exclude = ['created', 'updated', 'deleted']
        read_only = ['id']
