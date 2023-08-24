from django.urls import include, path
# from rest_framework import routers
from APIS.users.views.users_views import MyUsersGenericAPIView

# router = routers.DefaultRouter()
# router.register(r'users', users_views.userCreate, basename='user')

urlpatterns = [
    path('users/create/', MyUsersGenericAPIView.as_view(), name='user_create'),
]