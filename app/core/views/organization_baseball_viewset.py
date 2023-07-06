from datetime import datetime
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from baseball.models.competition import Competition
from baseball.serializers.competition_serializer import CompetitionSerializer
from baseball.models.team import Team
from baseball.serializers.team_serializer import TeamSerializer

class OrganizationBaseballCompetitionViewset (ModelViewSet):
    """Views for baseball competition endpoints for an organization.
    """
    serializer_class = CompetitionSerializer

    def list(self, request: Request, organization_id: str, *args, **kwargs) -> Response:
        """View a list of all competitions associated with the given organization.
        """
        competitions = Competition.objects.filter(organizer=organization_id)
        serializer = self.serializer_class(competitions, many=True)
        return Response(
            data=serializer.data, 
            status=status.HTTP_200_OK
        )
    
    def create(self, request: Request, organization_id: str,  *args, **kwargs) -> Response:
        """Create a new competition associated with the given organization.
        """
        request.data.update(organizer=organization_id)

        serializer = self.serializer_class(data=request.data)
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
    
    def retrieve(self, request: Request, organization_id: str, competition_id: str, *args, **kwargs) -> Response:
        """Get the details of a specific competition by uuid if it is associated with the given organization.
        """
        try:
            competition = Competition.objects.get(id=competition_id, organizer=organization_id)
            serializer = self.serializer_class(competition)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        except Competition.DoesNotExist:
            return Response(
                data={'status':f'Competition with id \'{competition_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def partial_update(self, request: Request, organization_id: str, competition_id: str, *args, **kwargs) -> Response:
        """Edit the details of a specific competition by uuid and organization.
        """
        if not request.data:
            return Response(
                data={
                    'status':'no fields were given to update',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            competition: Competition = Competition.objects.get(id=competition_id, organizer=organization_id)
            competition.updated = datetime.now()

            serializer = self.serializer_class(competition, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    data=serializer.data,
                    status=status.HTTP_200_OK,
                )
            else: 
                return Response(
                    data=serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Competition.DoesNotExist:
            return Response(
                data={'status': f'Competition with id \'{competition_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND,
            )

    def destroy(self, request: Request, organization_id: str, competition_id: str, *args, **kwargs) -> Response:
        """Delete the competition with the given uuid if it is associated with the given organization.
        """
        try:
            competition = Competition.objects.get(id=competition_id, organizer=organization_id)
            competition.delete()
            return Response(
                data={'status':'Competition deleted successfully'},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Competition.DoesNotExist:
            return Response(
                data={'status': f'Competition with id \'{competition_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND,
            )

class OrganizationBaseballTeamViewset(ModelViewSet):
    """Views for baseball team endpoints for an organization.
    """
    serializer_class = TeamSerializer

    def list(self, request: Request, organization_id: str, *args, **kwargs) -> Response:
        """View the list of all teams associated with the given organization.
        """
        teams = Team.objects.filter(organization=organization_id)
        serializer = self.serializer_class(teams, many=True)
        return Response(
            data=serializer.data, 
            status=status.HTTP_200_OK
        )
    
    def create(self, request: Request, organization_id: str, *args, **kwargs) -> Response:
        """Create a new team associated with the given organization.
        """
        request.data.update(organization=organization_id)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
    
    def retrieve(self, request: Request, organization_id: str, team_id: str, *args, **kwargs) -> Response:
        """Get the details of a specific team by uuid if it is associated with the given organization.
        """
        try:
            team = Team.objects.get(id=team_id, organization=organization_id)
            serializer = self.serializer_class(team)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK,
            )
        except Team.DoesNotExist:
            return Response(
                data={'status': f'Team with id \'{team_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND,
            )
    
    def partial_update(self, request: Request, organization_id: str, team_id: str, *args, **kwargs) -> Response:
        """Edit the details of a specific team by uuid if it is associated with the given organization.
        """
        if not request.data:
            return Response(
                data={
                    'status':'no fields were given to update',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            team: Team = Team.objects.get(id=team_id, organization=organization_id)
            team.updated = datetime.now()

            serializer = self.serializer_class(team, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    data=serializer.data,
                    status=status.HTTP_200_OK,
                )
            else: 
                return Response(
                    data=serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Team.DoesNotExist:
            return Response(
                data={'status': f'Team with id \'{team_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND,
            )
    
    def destroy(self, request: Request, organization_id: str, team_id: str, *args, **kwargs) -> Response:
        """Delete the team with the given uuid.
        """
        try:
            team = Team.objects.get(id=team_id, organization=organization_id)
            team.delete()
            return Response(
                data={'status':'Team deleted successfully'},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Team.DoesNotExist:
            return Response(
                data={'status': f'Team with id \'{team_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND
            )