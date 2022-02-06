from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'api/user_sessions', SessionsViewSet, basename='user_sessions')

urlpatterns = router.urls
