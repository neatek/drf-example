import enum
from django.db import models


from django.contrib.auth.models import User



class Project(models.Model):
    name = models.CharField(max_length=86)

@enum.unique
class TodoStatus(int, enum.Enum):
    Waiting = 1
    InProgress = 2
    Done = 3
    Closed = 4

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]


class Todo(models.Model):
    task = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.SmallIntegerField("status", choices=TodoStatus.choices())
    deadline = models.DateField()
