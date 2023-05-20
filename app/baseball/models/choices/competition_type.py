from django.db import models

class CompetitionType (models.IntegerChoices):
    """Choices for the different types of competitions.
    """
    SEASON = 1, 'Season'
    TOURNAMENT = 2, 'Tournament'
