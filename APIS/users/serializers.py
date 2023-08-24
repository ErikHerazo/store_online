from .models import OnlineStoreUsers
from rest_framework import serializers
from django.core.validators import EmailValidator


class OnlineStoreUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineStoreUsers
        fields = '__all__'

class MyUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    identification_number = serializers.IntegerField()
    email = serializers.EmailField(allow_blank=True, validators=[EmailValidator(message="Please enter a valid email address.")])