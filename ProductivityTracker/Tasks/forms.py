from django.forms import ModelForm
from django import forms
from .models import Task

class CreateTaskForm(ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'description', 'progress_status']