from rest_framework import viewsets, mixins
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import filters, status
from .models import Todo, Project
from .serializers import TodoSerializer, ProjectSerializer
from .models import TodoStatus
from .serializers import UserModelSerializer, UserModelSerializerVersion2


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TodoViewset(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["project"]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = int(TodoStatus.Closed)
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectViewset(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class UserModelViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == "2.0":
            return UserModelSerializerVersion2
        return UserModelSerializer
