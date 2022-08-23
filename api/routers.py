from rest_framework.routers import DefaultRouter

from api.viewsets import *

router = DefaultRouter()
router.register('technology', TechnologyGenericViewSet, basename='technology')

urlpatterns = router.urls