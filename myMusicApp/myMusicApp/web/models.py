from django.core import validators
from django.db import models

from myMusicApp.validators.validators import validate_only_letters


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15
    USERNAME_MIN_LENGTH = 2
    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=[
            validators.MinLengthValidator(USERNAME_MIN_LENGTH),
            validate_only_letters,
        ],
    )

    email = models.EmailField()

    age = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            validators.MinValueValidator(AGE_MIN_VALUE)
        ],
    )


class Album(models.Model):
    NAME_MAX_LENGTH = 30
    ARTIST_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30
    PRICE_MIN_VALUE = 0.0
    GENRES = (
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other'),
    )

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_MAX_LENGTH,
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=GENRES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image = models.URLField()

    price = models.FloatField(
        validators=[
            validators.MinValueValidator(PRICE_MIN_VALUE),
        ],
    )
