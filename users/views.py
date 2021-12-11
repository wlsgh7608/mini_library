from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from core.utils import LoginConfirm



from .serializers import UserSerializer
# Create your views here.

User = get_user_model()
class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer



class NickName(APIView):
    """
    nickname return
    """
    @LoginConfirm
    def get(self,request):
        return Response({"nickname":request.user.nickname})


    

