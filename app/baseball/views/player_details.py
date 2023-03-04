from datetime import datetime
from copy import deepcopy
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.player import Player
from ..serializers.player_serializer import PlayerSerializer

class PlayerDetails (APIView):
    """View, edit, and delete endpoints for the Player model.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request: Request, player_id: str, format=None) -> Response:
        """Get the details of a specific player by uuid.
        """
        try:
            player = Player.objects.get(id=player_id)
            serializer = PlayerSerializer(player)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK,
            )
        except Player.DoesNotExist:
            return Response(
                data={'status': f'Player with id \'{player_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND,
            )

    def put(self, request: Request, player_id: str, format=None) -> Response:
        """Edit the details of a specific player by uuid.
        """
        if not request.data:
            return Response(
                data={
                    'status':'no fields were given to update',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            player: Player = Player.objects.get(id=player_id)
            player.updated = datetime.now()

            # give the current player's name to the serialzier if none is provided
            data = deepcopy(request.data)
            if not data.get('first_name', None):
                data.update(first_name=player.first_name)
            if not data.get('last_name', None):
                data.update(last_name=player.last_name)

            serializer = PlayerSerializer(player, data=data)
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
        except Player.DoesNotExist:
            return Response(
                data={'status': f'Player with id \'{player_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND,
            )

    def delete(self, request: Request, player_id: str, format=None) -> Response:
        """Delete the player with the given uuid.
        """
        try:
            player = Player.objects.get(id=player_id)
            player.delete()
            return Response(
                data={'status':'Player deleted successfully'},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Player.DoesNotExist:
            return Response(
                data={'status': f'Player with id \'{player_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND
            )