from datetime import datetime
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.coach import Coach
from ..serializers.coach_serializer import CoachSerializer

class CoachViewSet (ModelViewSet):
    """Views for the coach model.
    """
    serializer_class = CoachSerializer

    def list(self, request: Request, *args, **kwargs) -> Response:
        """View the list of all coaches.
        """
        coaches = Coach.objects.all()
        serializer = CoachSerializer(coaches, many=True)
        return Response(
            data=serializer.data, 
            status=status.HTTP_200_OK
        )
    
    def create(self, request: Request, *args, **kwargs) -> Response:
        """Create a new coach.
        """
        serializer = CoachSerializer(data=request.data)
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
        
    def retrieve(self, request: Request, coach_id: str, *args, **kwargs) -> Response:
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
    
    def partial_update(self, request: Request, coach_id: str, *args, **kwargs) -> Response:
        """Edit the details of a specific coach by uuid.
        """
        if not request.data:
            return Response(
                data={
                    'status':'no fields were given to update',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            coach: Coach = Coach.objects.get(id=coach_id)
            coach.updated = datetime.now()

            serializer = CoachSerializer(coach, data=request.data, partial=True)
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
        
    def destroy(self, request: Request, coach_id: str, *args, **kwargs) -> Response:
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