from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.coach_competition_stats import CoachCompetitionStats
from ..serializers.coach_competition_stats_serializer import CoachCompetitionStatsSerializer

class CoachCompetitionStatsList (APIView):
    """List and create endpoints for the CoachCompetitionStats model.
    """
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, competition_id:str, request: Request, format=None) -> Response:
        """View the list of all coaches' stats for the given competition id.
        """
        coach_stats = CoachCompetitionStats.objects.filter(competition__id=competition_id)
        serializer = CoachCompetitionStatsSerializer(coach_stats, many=True)
        return Response(
            data=serializer.data, 
            status=status.HTTP_200_OK
        )

    def post(self, competition_id: str, coach_id: str, request: Request, format=None) -> Response:
        """Create a new coach competition stats object for the given competition id and coach id.
        """
        request.data.update('competition_id', competition_id)
        request.data.update('coach_id', coach_id)
        serializer = CoachCompetitionStatsSerializer(data=request.data)
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