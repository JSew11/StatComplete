from rest_framework import serializers

from ..models.coach_competition_stats import CoachCompetitionStats

class CoachStatsSerializer(serializers.ModelSerializer):
    """Serializer for the CoachCompetitionStats model.
    """

    class Meta:
        model = CoachCompetitionStats
        fields = '__all__'