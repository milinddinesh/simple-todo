from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import TaskViewSet
# from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'', TaskViewSet, basename='task')

urlpatterns = [
    path('create/',views.create_task, name='create_task'),
    path('update/<int:task_id>', views.update_task, name='update_task'),
    path('', include(router.urls)),
    
]