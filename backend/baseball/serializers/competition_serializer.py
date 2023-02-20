from rest_framework import serializers

from ..models.competition import Competition



class CompetitionSerializer (serializers.ModelSerializer):
    """Custom relational serializer for a coach's stats by competition.
    """

    class Meta:
        model = Competition
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']