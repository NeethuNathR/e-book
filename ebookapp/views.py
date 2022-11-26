import token

from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
import json
from .serializer import BookSerializer,UserSerializer
from .models import Books
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import get_user_model, authenticate
from rest_framework.generics import CreateAPIView

class CreateUserview(CreateAPIView):
    model=get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class BookViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset=Books.objects.all()
    serializer_class=BookSerializer


#@csrf_exempt
#def login(request):

 #  json_dict = json.loads(request.body)
  #  print(json_dict)
   # username =json_dict['username']
   # password =json_dict['password']
    #user = authenticate(username=username, password=password)
    #if user is not None:

     #  token,created=Token.objects.get_or_create(user=user)
      # print(token)
       #return JsonResponse({
        #   "token":token.key
       #})
