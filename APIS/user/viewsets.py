from .models import ModelUser
from rest_framework import viewsets
from .serializers import ModelUserSerializer
from rest_framework.request import Request

class ModelUserViewSet(viewsets.ModelViewSet):
    queryset = ModelUser.objects.all().order_by('id')
    serializer_class = ModelUserSerializer

    def create(self, request):
        data = request.data
        return "success"