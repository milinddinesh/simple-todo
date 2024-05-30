from django.db import models

class Quotes(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return f'"{self.quote}" - {self.author}'
