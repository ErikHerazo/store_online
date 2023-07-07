from django.urls import include, path
from rest_framework import routers
from .viewsets import ModelUserViewSet

router = routers.SimpleRouter()
router.register(r'user', ModelUserViewSet)

urlpatterns = router.urls