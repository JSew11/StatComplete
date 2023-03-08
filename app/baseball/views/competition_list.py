from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.competition import Competition
from ..serializers.competition_serializer import CompetitionSerializer

class CompetitionList (APIView):
    """List and create API endpoints for the competition model.
    """
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request: Request, format=None) -> Response:
        """View a list of all competitions.
        """
        competitions = Competition.objects.all()
        serializer = CompetitionSerializer(competitions, many=True)
        return Response(
            data=serializer.data, 
            status=status.HTTP_200_OK
        )