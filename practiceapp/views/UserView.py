from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from practiceapp.Serializers.UserSerializer import UserSerializer


class UserView(APIView):
    def get(self,request):
        UserData=User.objects.filter(username__contains=request.GET.get('username'))
        UserDict=[]
        for user in UserData:
            Id=User.objects.get(username=user).pk
            UserDict.append({"Id":Id,"UserName":user})
            #UserDict.update({"Id":Id,"UserName":user})
        print("UserDict",UserDict)
        return Response()


