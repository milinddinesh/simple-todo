from .models import Task
from rest_framework import serializers
# from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Task
        fields = ['id', 'title', 'due_date', 'created_date', 'description', 'progress_status','owner']

