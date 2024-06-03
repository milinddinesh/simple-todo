from typing import Any
from django.shortcuts import render
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from Tasks.models import Task
from Streaks.models import Streak

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

        try:
            first_streak = Streak.objects.filter(owner=self.request.user).first()
            if first_streak:
                streak_data = {
                    'title': first_streak.title,
                    'days': first_streak.days,
                    'id' : first_streak.id,
                    # Add other desired fields here
                }
                context['streak'] = streak_data
            else:
                context['streak'] = None
        except Streak.DoesNotExist:
            context['streak'] = None

        return context
    

class TaskView(LoginRequiredMixin, TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(owner=self.request.user)  # Adjust the filter if needed
        return context
