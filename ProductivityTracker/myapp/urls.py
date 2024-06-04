from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, HomeView, TaskView ,StreakView

router = DefaultRouter()
router.register(r'',UserViewSet)

urlpatterns = [
    path("",HomeView.as_view(), name='home'),
    path("view/task/",TaskView.as_view(),name='view_task'),
    path('view/streak/',StreakView.as_view(),name='streak-view'),
    path('user/', include(router.urls)),
    path("accounts/", include("django.contrib.auth.urls")),
]   