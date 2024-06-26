from rest_framework.routers import DefaultRouter
from .views import SpecificationViewSet, GroupViewSet, ComponentViewSet

router = DefaultRouter()
router.register(r"specifications", SpecificationViewSet)
router.register(r"groups", GroupViewSet)
router.register(r"components", ComponentViewSet)

urlpatterns = router.urls
