from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from ..models.competition import Competition
from ..serializers.competition_serializer import CompetitionSerializer

class CompetitionDetails (APIView):
    """View, edit, and delete endpoints for the competition model.
    """

    def get(self, request: Request, competition_id: str, format=None) -> Response:
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
        
    def put(self, request: Request, competition_id: str, format=None) -> Response:
        """Edit the details of a specific competition by uuid.
        """

    def delete(self, request:Request, competition_id: str, format=None) -> Response:
        """Delete the competition with the given uuid.
        """