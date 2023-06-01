from django.shortcuts import render
from rest_framework import viewsets, status

from accounts.serializers import Userserializers
from accounts.models import CustomUser

class UserViewSet(viewsets.ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = Userserializers