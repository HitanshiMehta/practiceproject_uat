from django.utils import timezone
from rest_framework import serializers
from rest_framework.fields import empty
from rest_framework.validators import UniqueForYearValidator

from practiceapp.models.MovieModel import Movie


class MovieSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    def __init__(self, instance=None, data=empty, **kwargs):
        fields = kwargs.pop('fields', None)

        super().__init__(instance, data, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Movie
        fields = "__all__"
        Validators = [
            UniqueForYearValidator(
                queryset=Movie.objects.all(),
                field='title',
                date_field='release_date',
                message='You can release only one movie per year.'
            )
        ]

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['release_date'] > data['end_date']:
            raise serializers.ValidationError("end date must occur after release date")
        return data
