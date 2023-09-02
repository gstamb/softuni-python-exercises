from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from games_play_app.play_app.models.profile_model import Profile


class Game(models.Model):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    PUZZLE = "Puzzle"
    STRATEGY = "Strategy"
    SPORTS = "Sports"
    BOARD = "Board/Card Game"
    OTHER = "Other"
    DEFAULT = '---------'

    GAMES_CHOICES = [
        (ACTION, "Action"),
        (ADVENTURE, "Adventure"),
        (PUZZLE, "Puzzle"),
        (STRATEGY, "Strategy"),
        (SPORTS, "Sports"),
        (BOARD, "Board/Card Game"),
        (OTHER, "Other"),
        (DEFAULT, '---------'),
    ]
    TITLE_MAX_LEN = 30

    RATING_MIN_VAL = 0.1
    RATING_MAX_VAL = 5.0
    RATING_ERR_MSG = f"Rating must be between {RATING_MIN_VAL} and {RATING_MAX_VAL}"

    LEVEL_MIN_VAL = 1
    LEVEL_ERR_MSG = f'Level value must be at least {LEVEL_MIN_VAL}'

    title = models.CharField(
        blank=False,
        max_length=TITLE_MAX_LEN,
        unique=True
    )
    category = models.CharField(
        blank=False,
        max_length=15,
        choices=GAMES_CHOICES

    )
    rating = models.FloatField(
        blank=False,
        validators=[MinValueValidator(RATING_MIN_VAL, RATING_ERR_MSG), MaxValueValidator(
            RATING_MAX_VAL, RATING_ERR_MSG)],

    )
    max_level = models.IntegerField(
        blank=True,
        validators=[MinValueValidator(LEVEL_MIN_VAL, LEVEL_ERR_MSG),],
        verbose_name='Max Level'
    )
    image_url = models.URLField(
        blank=False,
        verbose_name='Image URL'
    )
    summary = models.TextField(
        blank=True,
    )
