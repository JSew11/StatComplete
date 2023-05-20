from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from ..models.user import User

@api_view(['POST'])
def check_username_available(request: Request, format=None) -> Response:
    """Check if a username is available (if no existing user has it).
    """
    if username := request.data.get('username', None):
        existing_users = User.objects.filter(username=username).all()
        if existing_users.count() > 0:
            return Response(
                data={
                    'username_available': False
                },
                status=status.HTTP_200_OK
            )
        return Response(
            data={
                'username_available': True
            },
            status=status.HTTP_200_OK
        )
    return Response(
        data={
            'status': 'No username given'
        },
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
def check_email_available(request: Request, format=None) -> Response:
    """Check if an email is available (if no existin user has it).
    """
    if email := request.data.get('email', None):
        existing_users = User.objects.filter(email=email).all()
        if existing_users.count() > 0:
            return Response(
                data={
                    'email_available': False
                },
                status=status.HTTP_200_OK
            )
        return Response(
            data={
                'email_available': True
            },
            status=status.HTTP_200_OK
        )
    return Response(
        data={
            'status': 'No email given'
        },
        status=status.HTTP_400_BAD_REQUEST
    )