from rest_framework import serializers

from practiceapp.models.ProductModel import ProductModel


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields= "__all__"

    def create(self,validate_data):
        return ProductModel.objects.create(**validate_data)

