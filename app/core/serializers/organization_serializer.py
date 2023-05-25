from rest_framework import serializers

from ..models.organization import Organization

class OrganizationSerializer (serializers.ModelSerializer):
    """Serializer for the organization model.
    """
    competitions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    teams = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Organization
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']