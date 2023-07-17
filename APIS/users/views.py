from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import OnlineStoreUsers
from rest_framework import viewsets
from .serializers import OnlineStoreUserSerializer

class OnlineStoreUsersViewSet(viewsets.ModelViewSet):
    queryset = OnlineStoreUsers.objects.all().order_by('id')
    serializer_class = OnlineStoreUserSerializer

    def post(self, request):
        print(request)