from rest_framework.routers import DefaultRouter
from annotation.views import ImageViewSet, AnnotationViewSet

router = DefaultRouter()
router.register(r'images', ImageViewSet)  # /images/ and /images/{id}/
router.register(r'annotations', AnnotationViewSet)  # /annotations/ and /annotations/{id}/

urlpatterns = router.urls
