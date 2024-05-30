from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
# from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]