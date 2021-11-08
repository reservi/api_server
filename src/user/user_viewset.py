from django.db import models
from rest_framework import viewsets

from src.models.user import User
from .user_serializer import UserRegisterSerializer

class UserRegisterViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer