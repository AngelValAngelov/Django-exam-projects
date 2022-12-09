from django.core import validators
from django.db import models

from expenses_tracker.validators.validators import validate_only_letters, MaxFileSizeInMbValidator


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 15
    FIRST_NAME_MIN_LENGTH = 2

    LAST_NAME_MAX_LENGTH = 15
    LAST_NAME_MIN_LENGTH = 2

    MIN_VALUE_VALIDATOR = 0
    IMAGE_MAX_SIZE_IN_MB = 5

    first_name = models.CharField(
        max_length=15,
        validators=[
            validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        ]
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            validators.MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        ]
    )

    budget = models.FloatField(
        default=MIN_VALUE_VALIDATOR,
        validators=[
            validators.MinValueValidator(MIN_VALUE_VALIDATOR),
        ]
    )

    profile_image = models.ImageField(
        upload_to='profiles/',
        null=True,
        blank=True,
        validators=[
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        ],
    )


class Expense(models.Model):
    TITLE_MAX_CHARACTERS = 30

    title = models.CharField(
        max_length=TITLE_MAX_CHARACTERS,

    )

    image = models.URLField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.FloatField()


    class Meta:
        ordering = ('title', 'price',)