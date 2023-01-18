from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
# from django.http import Http404
from rest_framework import filters, status
from .models import Todo, Project
from .serializers import TodoSerializer, ProjectSerializer
from .models import TodoStatus


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TodoViewset(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['project']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = int(TodoStatus.Closed)
        instance.save()
        # self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


# class TodoStatusViewset(ModelViewSet):
#     queryset = TodoStatus.objects.all()
#     serializer_class = TodoStatusSerializer
#     pagination_class = TodoLimitOffsetPagination


class ProjectViewset(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name']
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
