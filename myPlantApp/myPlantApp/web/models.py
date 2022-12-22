from django.core import validators
from django.db import models

from myPlantApp.web.validators import start_with_capital_letter


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 10
    USERNAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MAX_LENGTH = 20

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=[
            validators.MinLengthValidator(USERNAME_MIN_LENGTH),
        ],
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        verbose_name='First Name',
        validators=[
            start_with_capital_letter,
        ],
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        verbose_name='Last Name',
        validators=[
            start_with_capital_letter,
        ],
    )
    picture = models.URLField(
        blank=True,
        null=True,
        verbose_name='Profile Picture'
    )


class Plant(models.Model):
    TYPE_MAX_LENGTH = 14
    TYPES = {
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants"),
    }
    NAME_MAX_LENGTH = 20
    NAME_MIN_LENGTH = 2

    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
        choices=TYPES,
    )
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=[
            validators.MinLengthValidator(NAME_MIN_LENGTH),
            start_with_capital_letter,
        ],
    )
    image = models.URLField(
        verbose_name='Image URL',
    )
    description = models.TextField()
    price = models.FloatField()

