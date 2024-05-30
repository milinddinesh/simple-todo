from django.shortcuts import render
from .serializers import UserSerializer
# from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


