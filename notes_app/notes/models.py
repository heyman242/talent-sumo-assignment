from django.db import models


class RegisteredUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Note(models.Model):
    TYPE_CHOICES = (
        ('text', 'Text'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    user = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE, related_name='notes')
    shared_with = models.ManyToManyField(RegisteredUser, related_name='shared_notes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




