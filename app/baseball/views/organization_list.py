from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.organization import Organization
from ..serializers.organization_serializer import OrganizationSerializer

class OrganizationList (APIView):
    """List and create API endpoints for the organization model.
    """
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request: Request, format=None) -> Response:
        """View a list of all organizations.
        """
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(
            data=serializer.data, 
            status=status.HTTP_200_OK
        )
    
    def post(self, request: Request, format=None) -> Response:
        """Create a new organization.
        """
        serializer = OrganizationSerializer(data=request.data)
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