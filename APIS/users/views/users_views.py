from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from utils.mongo_utils import MongoCRUD
from ..serializers import MyUserSerializer

class MyUsersGenericAPIView(APIView):
    # user creation method
    def post(self, request):
        user = request.data
        serialized_user = MyUserSerializer(data=user)
        
        if request.method == 'POST':
            try:
                if serialized_user.is_valid():
                    client = MongoCRUD('Users', 'users')
                    first_element_key = next(iter(user))
                    first_element_value = user.get(first_element_key)
                    first_element_type = type(first_element_value)
                    if first_element_type == list:
                        client.insertMultipleDocuments(first_element_value)
                        response = {
                            "msg":'the users were successfully registered',
                        }
                        return Response(response, status=status.HTTP_201_CREATED)
                    client.insertASingleDocument(user)
                    response = {
                        "msg":'the user was successfully registered',
                    }
                    return Response(response, status=status.HTTP_201_CREATED)  
                return Response(serialized_user.errors, status=status.HTTP_201_CREATED)
            except APIException as e:
                return Response({"detail": e.get_full_details()}, status=status.HTTP_400_BAD_REQUEST)            
        raise MethodNotAllowed(request.method)
        
    def get(self, request):
        pass