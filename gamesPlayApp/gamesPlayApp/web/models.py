from django.core import validators
from django.db import models


class Profile(models.Model):
    AGE_MIN_VALUE = 12
    PASSWORD_MAX_LENGTH = 30
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    email = models.EmailField()
    age = models.IntegerField(
        validators=[
            validators.MinValueValidator(AGE_MIN_VALUE),
        ],
    )
    password = models.CharField(
        max_length=PASSWORD_MAX_LENGTH,
    )
    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=FIRST_NAME_MAX_LENGTH,
        verbose_name='First Name',
    )
    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=LAST_NAME_MAX_LENGTH,
        verbose_name='Last Name',
    )
    picture = models.URLField(
        blank=True,
        null=True,
        verbose_name='Profile Picture',
    )


class Game(models.Model):
    TITLE_MAX_LENGTH = 30
    CATEGORY_MAX_LENGTH = 15
    RATING_MIN_VALUE = 0.1
    RATING_MAX_VALUE = 5.0
    MAX_LEVEL_MIN_VALUE = 1
    CATEGORY = {
        ("Action", "Action"),
        ("Adventure", "Adventure"),
        ("Puzzle", "Puzzle"),
        ("Strategy", "Strategy"),
        ("Sports", "Sports"),
        ("Board/Card Game", "Board/Card Game"),
        ("Other", "Other"),
    }

    title = models.CharField(
        unique=True,
        max_length=TITLE_MAX_LENGTH,
    )
    category = models.CharField(
        max_length=CATEGORY_MAX_LENGTH,
        choices=CATEGORY
    )
    rating = models.FloatField(
        validators=[
            validators.MinValueValidator(RATING_MIN_VALUE),
            validators.MaxValueValidator(RATING_MAX_VALUE),
        ]
    )
    max_level = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            validators.MinValueValidator(MAX_LEVEL_MIN_VALUE),
        ],
        verbose_name='Max Level',
    )
    image = models.URLField(
        verbose_name='Image URL',
    )
    summery = models.TextField(
        blank=True,
        null=True,
    )
