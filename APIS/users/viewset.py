from django.http import JsonResponse
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
        first_element_key = next(iter(data))
        first_element_value = data.get(first_element_key)
        first_element_type = type(first_element_value)
        if first_element_type == list:
            client.insertMultipleDocuments(first_element_value)
            response = {
                "msg":'successful registrations',
            }
            return JsonResponse(response)
        response = {
            "msg":'successful registration',
        }
        client.insertASingleDocument(data)
        return JsonResponse(response)

    def get_queryset(self):
        request_data = self.request.data
        client = MongoCRUD('Users','users')
        cursor = client.searchDocuments(request_data)
        list_doc = [document for document in cursor]
        return list_doc