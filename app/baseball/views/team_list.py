from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.team import Team
from ..serializers.team_serializer import TeamSerializer

class TeamList (APIView):
    """List and create endpoints for the team model.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request: Request, format=None) -> Response:
        """View the list of all teams.
        """
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(
            data=serializer.data, 
            status=status.HTTP_200_OK
        )

    def post(self, request: Request, format=None) -> Response:
        """Create a new team.
        """
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