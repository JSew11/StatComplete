from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.competition_coach import CompetitionCoach
from ..serializers.competition_coach_serializer import CompetitionCoachSerializer

class CompetitionCoachList (APIView):
    """List and create API endpoints for the competition coach model.
    """
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request: Request, competition_id: str, format=None) -> Response:
        """View a list of all competitions.
        """
        competition_coaches = CompetitionCoach.objects.filter(competition__id=competition_id).all()
        serializer = CompetitionCoachSerializer(competition_coaches, many=True)
        return Response(
            data=serializer.data, 
            status=status.HTTP_200_OK
        )