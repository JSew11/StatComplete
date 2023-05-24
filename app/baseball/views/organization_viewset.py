from datetime import datetime
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.organization import Organization
from ..models.competition import Competition
from ..models.team import Team
from ..serializers.organization_serializer import OrganizationSerializer
from ..serializers.competition_serializer import CompetitionSerializer
from ..serializers.team_serializer import TeamSerializer

class OrganizationViewSet (ModelViewSet):
    """Views for the organization model.
    """
    serializer_class = OrganizationSerializer

    def list(self, request: Request, *args, **kwargs) -> Response:
        """View a list of all organizations.
        """
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(
            data=serializer.data, 
            status=status.HTTP_200_OK
        )
    
    def create(self, request: Request, *args, **kwargs) -> Response:
        """Create a new organization.
        """
        serializer = OrganizationSerializer(data=request.data)
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
    
    def retrieve(self, request: Request, organization_id: str, *args, **kwargs) -> Response:
        """Get the details of a specific organization by uuid.
        """
        try:
            organization = Organization.objects.get(id=organization_id)
            serializer = OrganizationSerializer(organization)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        except Organization.DoesNotExist:
            return Response(
                data={'status':f'Organization with id \'{organization_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def partial_update(self, request: Request, organization_id: str, *args, **kwargs) -> Response:
        """Edit the details of a specific organization by uuid.
        """
        if not request.data:
            return Response(
                data={
                    'status':'no fields were given to update',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            organization: Organization = Organization.objects.get(id=organization_id)
            organization.updated = datetime.now()

            serializer = OrganizationSerializer(organization, data=request.data, partial=True)
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
        except Organization.DoesNotExist:
            return Response(
                data={'status': f'Organization with id \'{organization_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND,
            )
    
    def destroy(self, request: Request, organization_id: str, *args, **kwargs) -> Response:
        """Delete the organization with the given uuid.
        """
        try:
            organization = Organization.objects.get(id=organization_id)
            organization.delete()
            return Response(
                data={'status':'Organization deleted successfully'},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Organization.DoesNotExist:
            return Response(
                data={'status': f'Organization with id \'{organization_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND,
            )

    # organization-competition endpoints
    def list_competitions(self, request: Request, organization_id: str, *args, **kwargs) -> Response:
        """View a list of all competitions associated with the given organization.
        """
        competitions = Competition.objects.filter(organizer=organization_id)
        serializer = CompetitionSerializer(competitions, many=True)
        return Response(
            data=serializer.data, 
            status=status.HTTP_200_OK
        )
    
    def create_competition(self, request: Request, organization_id: str,  *args, **kwargs) -> Response:
        """Create a new competition associated with the given organization.
        """
        request.data.update(organizer=organization_id)

        serializer = CompetitionSerializer(data=request.data)
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
    
    def retrieve_competition(self, request: Request, organization_id: str, competition_id: str, *args, **kwargs) -> Response:
        """Get the details of a specific competition by uuid if it is associated with the given organization.
        """
        try:
            competition = Competition.objects.get(id=competition_id, organizer=organization_id)
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
    
    def partial_update_competition(self, request: Request, organization_id: str, competition_id: str, *args, **kwargs) -> Response:
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

            serializer = CompetitionSerializer(competition, data=request.data, partial=True)
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

    def destroy_competition(self, request: Request, organization_id: str, competition_id: str, *args, **kwargs) -> Response:
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
    
    # organization-team endpoints
    def list_teams(self, request: Request, organization_id: str, *args, **kwargs) -> Response:
        """View the list of all teams associated with the given organization.
        """
        teams = Team.objects.filter(organization=organization_id)
        serializer = TeamSerializer(teams, many=True)
        return Response(
            data=serializer.data, 
            status=status.HTTP_200_OK
        )
    
    def create_team(self, request: Request, organization_id: str, *args, **kwargs) -> Response:
        """Create a new team associated with the given organization.
        """
        request.data.update(organization=organization_id)

        serializer =TeamSerializer(data=request.data)
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
    
    def retrieve_team(self, request: Request, organization_id: str, team_id: str, *args, **kwargs) -> Response:
        """Get the details of a specific team by uuid if it is associated with the given organization.
        """
        try:
            team = Team.objects.get(id=team_id, organization=organization_id)
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
    
    def partial_update_team(self, request: Request, organization_id: str, team_id: str, *args, **kwargs) -> Response:
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

            serializer = TeamSerializer(team, data=request.data, partial=True)
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
    
    def destroy_team(self, request: Request, organization_id: str, team_id: str, *args, **kwargs) -> Response:
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