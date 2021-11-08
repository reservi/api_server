from rest_framework import serializers
from src.models import UserModel

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email', 'name', 'secondname', 'surename', 'country_name', 'country_short_name', 'country_image_url', 'sex_full', 'sex_shortcut')