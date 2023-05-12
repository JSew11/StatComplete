from datetime import datetime
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions

from ..models.competition import Competition
from ..models.competition_team import CompetitionTeam
from ..models.team_coach import TeamCoach
from ..serializers.competition_serializer import CompetitionSerializer
from ..serializers.competition_team_serializer import CompetitionTeamSerializer
from ..serializers.team_coach_serializer import TeamCoachSerializer
from ..serializers.team_player_serializer import TeamPlayerSerializer

class CompetitionViewSet (ModelViewSet):
    """Views for the competition model.
    """
    serializer_class = CompetitionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request: Request, *args, **kwargs) -> Response:
        """View a list of all competitions.
        """
        competitions = Competition.objects.all()
        serializer = CompetitionSerializer(competitions, many=True)
        return Response(
            data=serializer.data, 
            status=status.HTTP_200_OK
        )

    def retrieve(self, request: Request, competition_id: str, *args, **kwargs) -> Response:
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
    
    # competition team endpoints
    def list_teams(self, request: Request, competition_id: str, *args, **kwargs) -> Response:
        """View all the teams participating in the given competition.
        """
        try:
            competition: Competition = Competition.objects.get(id=competition_id)
            serializer = CompetitionTeamSerializer(competition.teams, many=True)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        except Competition.DoesNotExist:
            return Response(
                data={'status':f'Competition with id \'{competition_id}\' not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    def register_team(self, request: Request, competition_id: str, team_id: str, *args, **kwargs) -> Response:
        """Create a competition team for the given competition and team.
        """
        competition_team_data = {
            'competition': competition_id,
            'team': team_id
        }
        serializer = CompetitionTeamSerializer(data=competition_team_data)
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
        
    def retrieve_team(self, request: Request, competition_id: str, team_id: str, *args, **kwargs) -> Response:
        """Get the details of a specific competition team.
        """
        try:
            competition_team: CompetitionTeam = CompetitionTeam.objects.get(competition=competition_id, team=team_id)
            serializer : CompetitionTeamSerializer = CompetitionTeamSerializer(competition_team)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        except CompetitionTeam.DoesNotExist:
            return Response(
                data={'status': f'No team with the id \'{team_id}\' is registered for the competition with the id \'{competition_id}\''},
                status=status.HTTP_404_NOT_FOUND,
            )
    
    def update_team_record(self, request: Request, competition_id: str, team_id: str, *args, **kwargs) -> Response:
        """Update the competition team's record for the given cometition and team.
        """
        try:
            competition_team: CompetitionTeam = CompetitionTeam.objects.get(competition=competition_id, team=team_id)
            competition_team.updated = datetime.now()

            # TODO: dispatch a job to update the competition team record, team total record, and head coach record (team coach and coach models - possibly another job?)
            # for now just update the current competition team's record
            wins = int(request.data.get('wins', 0))
            losses = int(request.data.get('losses', 0))
            ties = int(request.data.get('ties', 0))
            record = competition_team.record
            if len(record) == 0:
                record['wins'] = wins
                record['losses'] = losses
                record['ties'] = ties
            else:
                record['wins'] = int(record['wins']) + wins
                record['losses'] = int(record['losses']) + losses
                record['ties'] = int(record['ties']) + ties
            
            serializer = CompetitionTeamSerializer(competition_team, data={'record': record}, partial=True)
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
        except CompetitionTeam.DoesNotExist:
            return Response(
                data={'status': f'No team with the id \'{team_id}\' is registered for the competition with the id \'{competition_id}\''},
                status=status.HTTP_404_NOT_FOUND,
            )

    def unregister_team(self, request: Request, competition_id: str, team_id: str, *args, **kwargs) -> Response:
        """Delete the competition team for the given competition and team.
        """
        try:
            competition_team: CompetitionTeam = CompetitionTeam.objects.get(competition=competition_id, team=team_id)
            competition_team.delete()
            return Response(
                data={'status':'Competition Team deleted successfully'},
                status=status.HTTP_204_NO_CONTENT,
            )
        except CompetitionTeam.DoesNotExist:
            return Response(
                data={'status': f'No team with the id \'{team_id}\' is registered for the competition with the id \'{competition_id}\''},
                status=status.HTTP_404_NOT_FOUND,
            )
        
    # team coach endpoints
    def create_team_coach(self, request: Request, competition_id: str, team_id: str, coach_id: str, *args, **kwargs) -> Response:
        """Add the given coach to the given competition team's coaching staff.
        """
        try:
            competition_team: CompetitionTeam = CompetitionTeam.objects.get(competition=competition_id, team=team_id)
            team_coach_data = {
                'competition_team': competition_team.id,
                'coach': coach_id,
                'jersey_number': int(request.data.get('jersey_number')),
                'role': int(request.data.get('role', TeamCoach.CoachRole.COACH)), # TODO: validate this to make sure it is a valid role
            }
            serializer = TeamCoachSerializer(data=team_coach_data)
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
        except CompetitionTeam.DoesNotExist:
            return Response(
                data={'status': f'No team with the id \'{team_id}\' is registered for the competition with the id \'{competition_id}\''},
                status=status.HTTP_404_NOT_FOUND,
            )
    
    def partial_update_team_coach(self, request: Request, competition_id: str, team_id: str, coach_id: str, *args, **kwargs) -> Response:
        """Update the given team coach using the request data.
        """
        try:
            team_coach: TeamCoach = TeamCoach.objects.get(
                competition_team__competition=competition_id,
                competition_team__team=team_id,
                coach=coach_id
            )
            serializer: TeamCoachSerializer = TeamCoachSerializer(team_coach, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    data=serializer.data,
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    data=serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        except TeamCoach.DoesNotExist:
            return Response(
                data={'status': f'No coach with the id \'{coach_id}\' is on the team \'{team_id}\' registered for the competition \'{competition_id}\''},
                status=status.HTTP_404_NOT_FOUND,
            )
    
    def delete_team_coach(self, request: Request, competition_id: str, team_id: str, coach_id: str, *args, **kwargs) -> Response:
        """Remove the given coach from the competition team's coaching staff.
        """
        try:
            team_coach: TeamCoach = TeamCoach.objects.get(
                competition_team__competition=competition_id,
                competition_team__team=team_id,
                coach=coach_id
            )
            team_coach.left_team = datetime.now()
            return Response(
                data={'status':'Team Coach removed successfully'},
                status=status.HTTP_200_OK,
            )
        except TeamCoach.DoesNotExist:
            return Response(
                data={'status': f'No coach with the id \'{coach_id}\' is on the team \'{team_id}\' registered for the competition \'{competition_id}\''},
                status=status.HTTP_404_NOT_FOUND,
            )
    
    # team player endpoints
    def create_team_player(self, request: Request, competition_id: str, team_id: str, player_id: str, *args, **kwargs) -> Response:
        """Add the given player to the given competition team's roster.
        """
        try:
            competition_team: CompetitionTeam = CompetitionTeam.objects.get(competition=competition_id, team=team_id)
            team_player_data = {
                'competition_team': competition_team.id,
                'player': player_id,
                'jersey_number': int(request.data.get('jersey_number')),
            }
            serializer = TeamPlayerSerializer(data=team_player_data)
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
        except CompetitionTeam.DoesNotExist:
            return Response(
                data={'status': f'No team with the id \'{team_id}\' is registered for the competition with the id \'{competition_id}\''},
                status=status.HTTP_404_NOT_FOUND,
            )