from django.core import validators
from django.db import models


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 10
    USERNAME_MIN_LENGTH = 2
    AGE_MIN_VALUE = 18
    PASSWORD_MAX_LENGTH = 30
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=[
            validators.MinLengthValidator(USERNAME_MIN_LENGTH, "The username must be a minimum of 2 chars"),
        ],
    )
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

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Car(models.Model):
    TYPE_MAX_LENGTH = 10
    TYPES = {
        ("Sports Car", "Sports Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other"),
    }
    MODEL_MAX_LENGTH = 20
    MODEL_MIN_LENGTH = 2
    YEAR_MIN_VALUE = 1980
    YEAR_MAX_VALUE = 2023
    PRICE_MIN_VALUE = 1.00

    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
        choices=TYPES,
    )
    model = models.CharField(
        max_length=MODEL_MAX_LENGTH,
        validators=[
            validators.MinLengthValidator(MODEL_MIN_LENGTH),
        ],
    )
    year = models.IntegerField(
        validators=[
            validators.MinValueValidator(YEAR_MIN_VALUE, "Year must be between 1980 and 2023"),
            validators.MaxValueValidator(YEAR_MAX_VALUE, "Year must be between 1980 and 2023"),
        ],
    )
    image = models.URLField(
        verbose_name='Image URL',
    )
    price = models.FloatField(
        validators=[
            validators.MinValueValidator(PRICE_MIN_VALUE),
        ],
    )
