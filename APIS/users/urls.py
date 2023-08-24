from django.urls import include, path
# from rest_framework import routers
from APIS.users.views import users_views

# router = routers.DefaultRouter()
# router.register(r'users', users_views.userCreate, basename='user')

urlpatterns = [
    path('users/', users_views.userCreate, name='user_create'),
]