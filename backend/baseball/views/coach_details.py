from datetime import datetime
from copy import deepcopy
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from ..models.coach import Coach
from ..serializers.coach_serializer import CoachSerializer

class CoachDetails(APIView):
    """View, edit, and delete endpoints for the Coach model.
    """
    
    def get(self, request: Request, coach_id: str, format=None) -> Response:
        """Get the details of a specific coach by uuid.
        """
        try:
            coach = Coach.objects.get(id=coach_id)
            serializer = CoachSerializer(coach)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK,
            )
        except Coach.DoesNotExist:
            return Response(
                data={'status': f'Coach with id \'{coach_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND,
            )

    def put(self, request: Request, coach_id: str, format=None) -> Response:
        """Edit the details of a specific coach by uuid.
        """
        if not request.data:
            mutable_fields = []
            for field in Coach._meta.get_fields():
                if field.name not in Coach.UNAVAILABLE_FIELDS:
                    mutable_fields.append(field.name)
            return Response(
                data={
                    'status':'no fields were given to update',
                    'available fields': mutable_fields
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            coach = Coach.objects.get(id=coach_id)
            coach.updated = datetime.now()

            # give the current coach's name to the serialzier if none is provided
            if not request.data.get('first_name', None):
                request.data.update(first_name=coach.first_name)
            if not request.data.get('last_name', None):
                request.data.update(last_name=coach.last_name)

            serializer = CoachSerializer(coach, data=request.data)
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
        except Coach.DoesNotExist:
            return Response(
                data={'status': f'Coach with id \'{coach_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND,
            )

    def delete(self, request: Request, coach_id: str, format=None) -> Response:
        """Delete the coach with the given id.
        """
        try:
            coach = Coach.objects.get(id=coach_id)
            coach.delete()
            return Response(
                data={'status':'Coach deleted successfully'},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Coach.DoesNotExist:
            return Response(
                data={'status': f'Coach with id \'{coach_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND,
            )
