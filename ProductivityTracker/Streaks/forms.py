from django.forms import ModelForm
from django import forms
from .models import Streak

class CreateStreakForm(ModelForm):
    class Meta:
        model = Streak
        fields = ['title', 'days']