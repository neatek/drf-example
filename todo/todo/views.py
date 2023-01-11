from rest_framework.viewsets import ModelViewSet
from .models import Todo, TodoStatus, Project
from .serializers import TodoSerializer, TodoStatusSerializer, ProjectSerializer


class TodoViewset(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoStatusViewset(ModelViewSet):
    queryset = TodoStatus.objects.all()
    serializer_class = TodoStatusSerializer


class ProjectViewset(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
