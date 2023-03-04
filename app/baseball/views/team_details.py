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

    def put(self, request: Request, team_id: str, format=None) -> Response:
        """Edit the details of a specific team by uuid.
        """
        if not request.data:
            return Response(
                data={
                    'status':'no fields were given to update',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            team: Team = Team.objects.get(id=team_id)
            team.updated = datetime.now()

            # give the current team's name/location to the serialzier if none is provided
            data = deepcopy(request.data)
            if not data.get('location', None):
                data.update(location=team.location)
            if not data.get('name', None):
                data.update(name=team.name)

            serializer = TeamSerializer(team, data=data)
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

    def delete(self, request: Request, team_id: str, format=None) -> Response:
        """Delete the team with the given uuid.
        """
        try:
            team = Team.objects.get(id=team_id)
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