from rest_framework import serializers

from ..models.organization import Organization
from ..models.competition import Competition

class CompetitionsField (serializers.RelatedField):
    """Custom relational field for an organization's competitions.
    """
    def to_representation(self, value: Competition):
        competition_string = value.name
        if value.start_date:
            competition_string += f' ({value.start_date}'
            if value.end_date:
                competition_string += f'-{value.end_date})'
            else:
                competition_string += ')'


class OrganizationSerializer (serializers.ModelSerializer):
    """Serializer for the organization model.
    """
    competitions = CompetitionsField(many=True, read_only=True)

    class Meta:
        model = Organization
        exclude = ['created', 'updated', 'deleted']
        read_only_fields = ['id']