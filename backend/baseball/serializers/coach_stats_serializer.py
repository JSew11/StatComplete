from rest_framework import serializers

from ..models.coach_stats import CoachStats

class CoachStatsSerializer(serializers.ModelSerializer):
    """Serializer for the CoachStats model.
    """

    class Meta:
        model = CoachStats
        fields = '__all__'