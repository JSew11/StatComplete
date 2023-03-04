from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.organization import Organization
from ..serializers.organization_serializer import OrganizationSerializer

class OrganizationDetails (APIView):
    """View, edit, and delete endpoints for the organization model.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request: Request, organization_id: str, format=None) -> Response:
        """Get the details of a specific organization by uuid.
        """
        try:
            organization = Organization.objects.get(id=organization_id)
            serializer = OrganizationSerializer(organization)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        except Organization.DoesNotExist:
            return Response(
                data={'status':f'Organization with id \'{organization_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        
    def put(self, request: Request, organization_id: str, format=None) -> Response:
        """Edit the details of a specific organization by uuid.
        """
        if not request.data:
            return Response(
                data={
                    'status':'no fields were given to update',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            organization: Organization = Organization.objects.get(id=organization_id)
            organization.updated = datetime.now()

            # give the current organization's name and type to the serialzier if none is provided
            if not request.data.get('name', None):
                request.data.update(name=organization.name)

            serializer = OrganizationSerializer(organization, data=request.data)
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
        except Organization.DoesNotExist:
            return Response(
                data={'status': f'Organization with id \'{organization_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND,
            )

    def delete(self, request:Request, organization_id: str, format=None) -> Response:
        """Delete the organization with the given uuid.
        """
        try:
            organization = Organization.objects.get(id=organization_id)
            organization.delete()
            return Response(
                data={'status':'Organization deleted successfully'},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Organization.DoesNotExist:
            return Response(
                data={'status': f'Organization with id \'{organization_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND,
            )