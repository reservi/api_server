from django.db import models
from rest_framework import viewsets

from src.models import UserModel
from .user_serializer import UserRegisterSerializer

class UserRegisterViewset(viewsets.ModelViewSet):
    http_method_names = ['post']
    queryset = UserModel.objects.all()
    serializer_class = UserRegisterSerializer