from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'api/sessions', SessionsViewSet, basename='sessions')

urlpatterns = router.urls
