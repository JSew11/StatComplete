from django.db import models

class CoachRole (models.IntegerChoices):
    """Choices for the different coaching roles as a part of a team.
    """
    COACH = 0, 'Coach'
    MANAGER = 1, 'Manager'
    ASSISTANT = 2, 'Assistant Coach'
