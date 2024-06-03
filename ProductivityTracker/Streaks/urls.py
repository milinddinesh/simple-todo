from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StreakViewSet
from . import views

router = DefaultRouter()
router.register(r'', StreakViewSet,basename='streak')

urlpatterns = [
    path('create/',views.create_streak, name='create_streak'),
    path('update/<int:task_id>', views.update_streak, name='update_streak'),
    path('', include(router.urls)),
]