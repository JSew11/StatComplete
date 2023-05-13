from django.db import models

class FieldingPosition(models.IntegerChoices):
    """Choices for the different positions a player can play in the field.
    """
    PITCHER = 1, 'P'
    CATCHER = 2, 'C'
    FIRST_BASE = 3, '1B'
    SECOND_BASE = 4, '2B'
    THIRD_BASE = 5, '3B'
    SHORTSTOP = 6, 'SS'
    LEFT_FIELD = 7, 'LF'
    CENTER_FIELD = 8, 'CF'
    RIGHT_FIELD = 9, 'RF'