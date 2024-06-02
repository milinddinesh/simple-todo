from django.shortcuts import render
from .serializers import UserSerializer
# from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from Tasks.models import Task

# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        in_progress_tasks = Task.objects.filter(owner=self.request.user, progress_status=Task.IN_PROGRESS)
        context['in_progress_tasks'] = in_progress_tasks
        return context

