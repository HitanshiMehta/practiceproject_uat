from rest_framework.response import Response
from rest_framework.views import APIView

from practiceapp.Serializers.ProductSerializer import ProductSerializer
from practiceapp.models.ProductModel import ProductModel


class ProductView(APIView):
    def get(self,*args,**kwargs):
        Product=ProductModel.objects.all()
        serializer=ProductSerializer(Product,many=True)
        return Response({"articles":serializer.data})

    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        if(serializer.is_valid(raise_exception=True)):
            serializer.save()
        else:
            serializer.errors()
        return Response({"articles":serializer.data})

