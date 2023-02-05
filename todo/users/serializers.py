from rest_framework.serializers import HyperlinkedModelSerializer

# from .models import User
from django.contrib.auth.models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
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
