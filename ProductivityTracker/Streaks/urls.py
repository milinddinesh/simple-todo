from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StreakViewSet

router = DefaultRouter()
router.register(r'', StreakViewSet,basename='streak')

urlpatterns = [
    path('', include(router.urls)),
]