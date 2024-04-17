from rest_framework import routers
from .views import CRUDViewSet

router = routers.DefaultRouter()
router.register(r'crud', CRUDViewSet)
