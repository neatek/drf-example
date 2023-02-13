from rest_framework.serializers import HyperlinkedModelSerializer
from django.contrib.auth.models import User
from .models import Project, Todo


class ProjectSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        fields = ("id", "name")


class TodoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
        fields = ("id", "task", "status", "deadline", "project", "user")


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # fields = "__all__"
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
        )


class UserModelSerializerVersion2(HyperlinkedModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "is_superuser",
            "is_staff",
            "email",
        )
