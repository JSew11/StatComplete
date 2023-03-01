from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.competition import Competition
from ..serializers.competition_serializer import CompetitionSerializer

class CompetitionDetails (APIView):
    """View, edit, and delete endpoints for the competition model.
    """
    permission_classes = (permissions.IsAuthenticated,)

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
        if not request.data:
            return Response(
                data={
                    'status':'no fields were given to update',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            competition = Competition.objects.get(id=competition_id)
            competition.updated = datetime.now()

            # give the current competition's name and type to the serialzier if none is provided
            if not request.data.get('name', None):
                request.data.update(name=competition.name)
            if not request.data.get('type', None):
                request.data.update(type=competition.type)

            serializer = CompetitionSerializer(competition, data=request.data)
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

    def delete(self, request:Request, competition_id: str, format=None) -> Response:
        """Delete the competition with the given uuid.
        """
        try:
            competition = Competition.objects.get(id=competition_id)
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