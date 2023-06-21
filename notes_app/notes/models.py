from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    TYPE_CHOICES = (
        ('text', 'Text'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, related_name='shared_notes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

