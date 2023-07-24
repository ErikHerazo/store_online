from django.urls import include, path
from rest_framework import routers
from .viewset import OnlineStoreUsersViewSet 

router = routers.SimpleRouter()
router.register(r'users', OnlineStoreUsersViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = router.urls