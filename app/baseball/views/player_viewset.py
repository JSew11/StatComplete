from datetime import datetime
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.player import Player
from ..serializers.player_serializer import PlayerSerializer

class PlayerViewSet (ModelViewSet):
    """Views for the player model.
    """
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request: Request, *args, **kwargs) -> Response:
        """View the list of all players.
        """
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(
            data=serializer.data, 
            status=status.HTTP_200_OK
        )
    
    
    def create(self, request: Request, *args, **kwargs) -> Response:
        """Create a new player.
        """
        serializer =PlayerSerializer(data=request.data)
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
    
    def retrieve(self, request: Request, player_id: str, *args, **kwargs) -> Response:
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
    
    def partial_update(self, request: Request, player_id: str, *args, **kwargs) -> Response:
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

            serializer = PlayerSerializer(player, data=request.data, partial=True)
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
    
    def destroy(self, request: Request, player_id: str, *args, **kwargs) -> Response:
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