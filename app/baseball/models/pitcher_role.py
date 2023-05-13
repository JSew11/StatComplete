from django.db import models

class PitcherRole(models.IntegerChoices):
    """Choices for the different roles a pitcher can have.
    """
    STARTING_PITCHER = 0, 'SP'
    RELIEF_PITCHER = 1, 'RP'
