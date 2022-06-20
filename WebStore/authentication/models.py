from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    genders = [("male", "male"), ("female", "female")]
    image = models.ImageField("User's image", blank=True)
    age = models.PositiveIntegerField("User's age", default=0)
    address = models.CharField("Address", max_length=80)
    gender = models.CharField("Gender", choices=genders, max_length=6)

    def __str__(self):
        return self.first_name
