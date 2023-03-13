from rest_framework.routers import DefaultRouter
from .views import ProductViewModel

router = DefaultRouter()

router.register(r"product", ProductViewModel, basename="product")

new_pattern = router.urls