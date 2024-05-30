from rest_framework import serializers
from .models import  Streak

class StreakSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Streak
        fields = ['id', 'title', 'days','owner']

        
