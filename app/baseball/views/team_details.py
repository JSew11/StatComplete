from datetime import datetime
from copy import deepcopy
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.team import Team
from ..serializers.team_serializer import TeamSerializer

class TeamDetails (APIView):
    """View, edit, and delete endpoints for the team model.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request: Request, team_id: str, format=None) -> Response:
        """Get the details of a specific team by uuid.
        """
        try:
            team = Team.objects.get(id=team_id)
            serializer = TeamSerializer(team)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK,
            )
        except Team.DoesNotExist:
            return Response(
                data={'status': f'Team with id \'{team_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND,
            )
