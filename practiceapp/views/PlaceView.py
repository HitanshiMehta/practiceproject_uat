from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from practiceapp.Serializers.PlaceSerializer import PlaceSerializer
from practiceapp.entities import PlaceProxy
from practiceapp.models.PlaceModel import Place


class PlaceViews(APIView):
    def get(self,*args,**kwrgs):
        if kwrgs is not None:
            place=PlaceProxy.objects.filter_data(**kwrgs)
        else:
            place=Place.objects.get_all()
        serializer=PlaceSerializer(place,many=True)
        return Response({"Places":serializer.data},status=status.HTTP_200_OK)

    def post(self,request):
        serializer=PlaceSerializer(data=request.data)
        if(serializer.is_valid(raise_exception=True)):
            place_saved=serializer.save()
        else:
            raise APIException("There was a problem!")
        return Response({"success":"Place {} created successfully".format(place_saved)},status=status.HTTP_201_CREATED)

    def delete(self,*args,**kwargs):
        Place=PlaceProxy.objects.filter_data(**kwargs).delete()
        return Response({"Successfully deleted object {}".format(Place)},status=status.HTTP_204_NO_CONTENT)

