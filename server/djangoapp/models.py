# djangoapp/models.py

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# CarMake model
class CarMake(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Car Make Name"
    )  # Nom de la marque de voiture
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return f"{self.name} - {self.description}"


# CarModel model
class CarModel(models.Model):
    car_make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE,
        related_name="car_models",
        verbose_name="Car Make"
    )  # Relation Many-to-One avec CarMake
    name = models.CharField(max_length=100, verbose_name="Model Name")

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
    ]
    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        default='SUV',
        verbose_name="Type"
    )
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ],
        verbose_name="Year"
    )

    def __str__(self):
        return f"{self.name} ({self.type} - {self.year})"
