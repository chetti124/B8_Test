from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import  EmployeeModelView, StudentModelViewSet


router = DefaultRouter()
router.register(r'studs', StudentModelViewSet, basename='student'),
router.register(r'emps', EmployeeModelView, basename='employee'),

new_urlpatterns = router.urls
