from rest_framework import serializers

from ..models.coach import Coach

class CoachSerializer (serializers.ModelSerializer):
    """Serializer for the coach model.
    """
    
    class Meta:
        model = Coach
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']