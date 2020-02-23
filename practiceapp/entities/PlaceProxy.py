from practiceapp.managers.PlaceManager import PlaceManager
from practiceapp.models.PlaceModel import Place


class PlaceProxy(Place):
    objects = PlaceManager()
    class Meta:
        proxy=True