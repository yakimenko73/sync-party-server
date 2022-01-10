from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'api/rooms', RoomViewSet, basename='room')

urlpatterns = router.urls
