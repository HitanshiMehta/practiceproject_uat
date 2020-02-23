from django.test import TestCase

from practiceapp.models.PlaceModel import Place


class PlaceTestCase(TestCase):
    def test_get_all(self):
        Place.objects.get_all()

    def test_get_hitanshi(self):
        Place.objects.get_hitanshi()

    def test_create_place(self):
        Place.objects.create(name="hitanshi",address="surat")