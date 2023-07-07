from .models import ModelUser
from rest_framework import serializers

class ModelUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelUser
        fields = '__all__'