# from rest_framework import generics
from .models import Streak
from .serializers import StreakSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from myapp.permissions import IsOwnerOrReadOnly

class StreakViewSet(viewsets.ModelViewSet):
    # queryset = Streak.objects.all()
    serializer_class = StreakSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
    
    def get_queryset(self):
        return Streak.objects.filter(owner=self.request.user)

    @action(detail=True, methods=['get'])
    def count(self, request):
        streak_count = Streak.objects.filter(owner=self.request.user).count()
        return Response({'total_streaks': streak_count}, status=status.HTTP_200_OK)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'])
    def increment_days(self, request, pk=None):
        try:
            streak = self.get_object()
            if streak.owner != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)

            streak.days += 1
            streak.save()
            return Response({'days': streak.days}, status=status.HTTP_200_OK)
        except Streak.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
