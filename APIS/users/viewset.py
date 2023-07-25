import json
from django.shortcuts import render
from utils.mongo_utils import MongoCRUD

# Create your views here.
from .models import OnlineStoreUsers
from rest_framework import viewsets
from .serializers import OnlineStoreUserSerializer

class OnlineStoreUsersViewSet(viewsets.ModelViewSet):
    queryset = OnlineStoreUsers.objects.all().order_by('id')
    serializer_class = OnlineStoreUserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        client = MongoCRUD('Users', 'users')
        client.insertMultipleDocuments(data['data'])
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        request_data = self.request.data
        client = MongoCRUD('Users','users')
        cursor = client.searchDocuments(request_data)
        list_doc = [document for document in cursor]
        return list_doc