from .models import OnlineStoreUsers
from rest_framework import serializers

class OnlineStoreUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineStoreUsers
        fields = '__all__'