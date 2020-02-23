from django.db import models

from practiceapp.managers.PlaceManager import PlaceManager

class Place(models.Model):
    id=models.CharField(primary_key=True,max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    objects=PlaceManager()