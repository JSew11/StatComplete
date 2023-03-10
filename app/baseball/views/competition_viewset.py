from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.competition import Competition
from ..models.competition_team import CompetitionTeam
from ..serializers.competition_serializer import CompetitionSerializer
from ..serializers.competition_team_serializer import CompetitionTeamSerializer

class CompetitionViewSet (ModelViewSet):
    """Views for the competition model.
    """
    serializer_class = CompetitionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request: Request, *args, **kwargs) -> Response:
        """View a list of all competitions.
        """
        competitions = Competition.objects.all()
        serializer = CompetitionSerializer(competitions, many=True)
        return Response(
            data=serializer.data, 
            status=status.HTTP_200_OK
        )

    def retrieve(self, request: Request, competition_id: str, *args, **kwargs) -> Response:
        """Get the details of a specific competition by uuid.
        """
        try:
            competition = Competition.objects.get(id=competition_id)
            serializer = CompetitionSerializer(competition)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        except Competition.DoesNotExist:
            return Response(
                data={'status':f'Competition with id \'{competition_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    # competition team endpoints
    def register_team(self, request: Request, competition_id: str, team_id: str, *args, **kwargs) -> Response:
        """Create a competition team for the given competition and team.
        """
        competition_team_data = {
            'competition': competition_id,
            'team': team_id
        }
        serializer = CompetitionTeamSerializer(data=competition_team_data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def unregister_team(self, request: Request, competition_id: str, team_id: str, *args, **kwargs) -> Response:
        """Delete the competition team for the given competition and team.
        """
        try:
            competition_team: CompetitionTeam = CompetitionTeam.objects.get(competition=competition_id, team=team_id)
            competition_team.delete()
            return Response(
                data={'status':'Competition Team deleted successfully'},
                status=status.HTTP_204_NO_CONTENT,
            )
        except CompetitionTeam.DoesNotExist:
            return Response(
                data={'status': f'No competition team associated with the competition \'{competition_id}\' and team \'{team_id}\''},
                status=status.HTTP_404_NOT_FOUND,
            )