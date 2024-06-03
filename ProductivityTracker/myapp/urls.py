from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, HomeView, TaskView
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'',UserViewSet)

urlpatterns = [
    path("home/",HomeView.as_view(), name='home'),
    path('view/task/',TaskView.as_view(),name='task_view'),
    path('user/', include(router.urls)),
    path("accounts/", include("django.contrib.auth.urls")),
]