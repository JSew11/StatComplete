from django.db import models

class GameStatus (models.IntegerChoices):
    """Choices for the different statuses for a game.
    """
    SCHEDULED = 0, 'Scheduled'
    IN_PROGRESS = 1, 'In Progress'
    FINISHED = 2, 'Finished'
