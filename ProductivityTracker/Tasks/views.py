from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from myapp.permissions import IsOwnerOrReadOnly
from django.http import Http404

from django.shortcuts import render, redirect
from .forms import CreateTaskForm
from .models import Task

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    @action(detail=False, methods=['get'])
    def count(self, request):
        try:
            task_count = Task.objects.filter(owner=self.request.user).count()
            return Response({'total_tasks': task_count}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'])
    def completion_percentage(self, request):
        try:
            total_tasks = Task.objects.filter(owner=self.request.user).count()
            completed_tasks = Task.objects.filter(owner=self.request.user, progress_status=Task.DONE).count()

            if total_tasks == 0:
                percentage_completed = 0
            else:
                percentage_completed = (completed_tasks / total_tasks) * 100

            return Response({'completion_percentage': percentage_completed}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def in_progress(self, request):
        try:
            in_progress_tasks = Task.objects.filter(owner=self.request.user, progress_status=Task.IN_PROGRESS)
            serializer = TaskSerializer(in_progress_tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
def create_task(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  # Don't save immediately
            task.owner = request.user  # Assign current user as owner
            task.save()
            return redirect('/view/task')  # Redirect to success page after saving
    else:
        form = CreateTaskForm()

    return render(request, 'create-task.html', {'form': form})

@login_required
def update_task(request, task_id):
  try:
    task = get_object_or_404(Task, pk=task_id, owner=request.user)
  except Task.DoesNotExist:
    raise Http404("Task not found")

  if request.method == 'GET':
    serializer = TaskSerializer(task)
    context = {'task': serializer.data}  # Pass serialized data to context
    return render(request, 'update-task.html', context)
  else:
    return Http404("GET method expected") 