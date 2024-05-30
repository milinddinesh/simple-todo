from django.urls import path
from .views import MotivationalQuoteRetrieveView

urlpatterns = [
    path('<int:pk>/', MotivationalQuoteRetrieveView.as_view(), name='quote-detail'),
]
