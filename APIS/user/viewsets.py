from .models import ModelUser
from rest_framework import viewsets
from .serializers import ModelUserSerializer

class ModelUserViewSet(viewsets.ModelViewSet):
    queryset = ModelUser.objects.all().order_by('id')
    serializer_class = ModelUserSerializer