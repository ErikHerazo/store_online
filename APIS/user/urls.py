from django.urls import include, path
from rest_framework import routers
from .viewsets import ModelUserViewSet

router = routers.SimpleRouter()
router.register(r'users', ModelUserViewSet)

urlpatterns = router.urls