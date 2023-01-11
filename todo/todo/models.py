from django.db import models
from users.models import User

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=86)


class TodoStatus(models.Model):
    name = models.CharField(max_length=86)


class Todo(models.Model):
    task = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    status = models.OneToOneField(TodoStatus, on_delete=models.CASCADE)
    deadline = models.DateField()
