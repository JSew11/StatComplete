from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.team import Team
from ..serializers.team_serializer import TeamSerializer

class TeamViewSet (ModelViewSet):
    """Views for the team model.
    """
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request: Request, *args, **kwargs) -> Response:
        """View the list of all teams.
        """
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(
            data=serializer.data, 
            status=status.HTTP_200_OK
        )
    
    def retrieve(self, request: Request, team_id: str, *args, **kwargs) -> Response:
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