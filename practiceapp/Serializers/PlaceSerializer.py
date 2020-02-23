from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator

from practiceapp.entities import PlaceProxy
from practiceapp.models.PlaceModel import Place

class PlaceSerializer(serializers.ModelSerializer):

    #i'm the one...
    def check_name(value):
        if 'hitanshi' not in value.lower():
            raise serializers.ValidationError("Hitanshi name me hona j chahiye")

    def validate_address(self, value):
        if 'surat' not in value.lower():
            raise serializers.ValidationError("Address is not of surat")
        return value

    name=serializers.CharField(max_length=80,validators=[check_name])
    address=serializers.CharField(validators=[UniqueValidator(queryset=PlaceProxy.objects.get_all())])

    #validator comment added by bushra
    def validate(self, data):
        if data['name']=="hitanshiii":
            raise serializers.ValidationError("hitanshiii ma be i kem che?")
        return  data


    #Just to learn how to merge added by chitra
    #Just to learn how to merge
    class Meta:
        model= Place
        validators = [
            UniqueTogetherValidator(
                queryset=PlaceProxy.objects.get_all(),
                fields=['name', 'address']
            )
        ]
        fields = ('id','name','address')


        #create with manager added by masters
        #create with manager added by hitanshi
        #As new member i want to add comment : Dhvani
        #create with manager
        def create(self,validate_data):
            print("validate_data",validate_data)
            return Place.objects.create(**validate_data)




