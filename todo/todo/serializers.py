from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project, Todo, TodoStatus


class ProjectSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


# class TodoStatusSerializer(HyperlinkedModelSerializer):
#     class Meta:
#         model = TodoStatus
#         fields = '__all__'


class TodoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
