from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.competition_coach import CompetitionCoach
from ..serializers.competition_coach_serializer import CompetitionCoachSerializer

class CompetitionCoachDetails (APIView):
    """View, edit, and delete endpoints for the competition model.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request: Request, competition_id: str, coach_id: str, format=None) -> Response:
        """Get the details of a specific competition coach by uuid.
        """
        try:
            competition_coach = CompetitionCoach.objects.get(
                competition__id=competition_id,
                coach__id=coach_id
            )
            serializer = CompetitionCoachSerializer(competition_coach)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK,
            )
        except CompetitionCoach.DoesNotExist:
            return Response(
                data={'status': f'Coach with id \'{coach_id}\' not found in the competition \'{competition_id}\''},
                status=status.HTTP_404_NOT_FOUND,
            )

    def post(self, request: Request, competition_id: str, coach_id: str, format=None) -> Response:
        """Create a new competition coach with the associated competition and coach.
        """
        serializer = CompetitionCoachSerializer(data=request.data)
        request.data.update(coach=coach_id)
        request.data.update(competition=competition_id)
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

    def delete(self, request: Request, competition_id: str, coach_id: str, format=None) -> Response:
        """Delete the competition coach with the given uuid.
        """
        try:
            competition_coach: CompetitionCoach = CompetitionCoach.objects.get(competition__id=competition_id, coach__id=coach_id)
            # TODO: check if the competition coach has any team data before deleting
            competition_coach.delete()
            return Response(
                data={'status':'Competition coach deleted successfully'},
                status=status.HTTP_204_NO_CONTENT,
            )
        except CompetitionCoach.DoesNotExist:
            return Response(
                data={'status': f'Competition with id \'{competition_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND,
            )