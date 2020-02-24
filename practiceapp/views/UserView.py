from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User



class UserView(APIView):
    def get(self,request):
        UserData=User.objects.filter(username__contains=request.GET.get('username')).values()
        return JsonResponse({"User": list(UserData)})


