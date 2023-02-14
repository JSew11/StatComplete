from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from ..models.coach import Coach
from ..serializers.coach_serializer import CoachSerializer

class CoachList(APIView):
    """List and create endpoints for the Coach model.
    """
    
    def get(self, request: Request, format=None) -> Response:
        """View the list of all coaches.
        """
        coaches = Coach.objects.all()
        serializer = CoachSerializer(coaches, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, format=None) -> Response:
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