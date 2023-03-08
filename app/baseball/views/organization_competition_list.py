from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.competition import Competition
from ..serializers.competition_serializer import CompetitionSerializer

class OrganizationCompetitionList (APIView):
    """List and create API endpoints for the competition model.
    """
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request: Request, organization_id: str, format=None) -> Response:
        """View a list of all competitions.
        """
        competitions = Competition.objects.filter(organizer=organization_id)
        serializer = CompetitionSerializer(competitions, many=True)
        return Response(
            data=serializer.data, 
            status=status.HTTP_200_OK
        )
    
    def post(self, request: Request, organization_id: str, format=None) -> Response:
        """Create a new competition.
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