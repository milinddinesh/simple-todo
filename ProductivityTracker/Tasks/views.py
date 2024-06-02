from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from myapp.permissions import IsOwnerOrReadOnly

class TaskViewSet(viewsets.ModelViewSet):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
    
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    @action(detail=True, methods=['get'])
    def count(self, request):
        task_count = Task.objects.filter(owner=self.request.user).count()
        return Response({'total_tasks': task_count}, status=status.HTTP_200_OK)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'])
    def completion_percentage(self, request):
        total_tasks = Task.objects.filter(owner=self.request.user).count()
        completed_tasks = Task.objects.filter(owner=self.request.user, progress_status=Task.DONE).count()

        if total_tasks == 0:
            percentage_completed = 0
        else:
            percentage_completed = (completed_tasks / total_tasks) * 100

        return Response({'completion_percentage': percentage_completed}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def in_progress(self, request):
        in_progress_tasks = Task.objects.filter(owner=self.request.user, progress_status=Task.IN_PROGRESS)
        serializer = TaskSerializer(in_progress_tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

