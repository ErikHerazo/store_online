from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from utils.mongo_utils import MongoCRUD

@api_view(['POST'])    
def userCreate(request):
    data = request.data
    if request.method == 'POST':
        client = MongoCRUD('Users', 'users')
        first_element_key = next(iter(data))
        first_element_value = data.get(first_element_key)
        first_element_type = type(first_element_value)
        if first_element_type == list:
            client.insertMultipleDocuments(first_element_value)
            response = {
                "msg":'successful registrations',
            }
            return Response(response, status=status.HTTP_201_CREATED)
        client.insertASingleDocument(data)
        response = {
            "msg":'successful registration',
        }
        return Response(response, status=status.HTTP_201_CREATED)
    response = {
        "message": 'wrong method'
    }    
    return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)