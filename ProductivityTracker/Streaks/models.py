from django.db import models

# Create your models here.
class Streak(models.Model):
    title = models.CharField(max_length=255)
    days = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='streaks',on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        options = {'title': self.title} if self.title else {}
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title