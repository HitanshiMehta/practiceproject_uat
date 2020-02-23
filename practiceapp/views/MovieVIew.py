from django.http import request
from rest_framework import mixins
from rest_framework.exceptions import APIException
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from practiceapp.Serializers.MovieSerializer import MovieSerializer
from practiceapp.models.MovieModel import Movie


class MovieDetailsView(APIView):

    def get(self, request,*args, **kwrgs):
        movie = Movie.objects.all()

        if len(request.GET) != 0:
            for i in request.GET:
                key=i
                serializer = MovieSerializer(movie, many=True, fields=('title', key))
        else:
            serializer = MovieSerializer(movie, many=True)

        return Response({"Movies": serializer.data})

    def post(self,request):
        serializer=MovieSerializer(data=request.data)
        if(serializer.is_valid(raise_exception=True)):
            place_saved=serializer.save()
        else:
            raise APIException("There was a problem!")
        return Response({"success":"Place {} created successfully".format(place_saved)})