from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
#from django.contrib.auth.models import AbstractUser

class Thing(models.Model):
    name = models.CharField(
    unique = True,
    max_length = 30,
    blank = False
    )
    description = models.CharField(
    max_length = 120,
    blank = True
    )
    quantity = models.PositiveIntegerField(
    default = 0,
    validators=[
    MinValueValidator(0),
    MaxValueValidator(100)
    ]
    )
