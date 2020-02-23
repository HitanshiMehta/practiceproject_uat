from django.db import models

from practiceapp.models.PlaceModel import Place


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)