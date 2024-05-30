from django.db import models

# Create your models here.
class Task(models.Model):
    TO_DO = 'to-do'
    IN_PROGRESS = 'in progress'
    DONE = 'done'
    
    PROGRESS_STATUS_CHOICES = [
        (TO_DO, 'To-Do'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
    ]

    title = models.CharField(max_length=255)
    due_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    progress_status = models.CharField(
        max_length=20,
        choices=PROGRESS_STATUS_CHOICES,
        default=TO_DO,
    )
    owner = models.ForeignKey('auth.User', related_name='tasks',on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        options = {'title': self.title} if self.title else {}
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
