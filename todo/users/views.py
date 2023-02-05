# from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, mixins
# from .models import User
from django.contrib.auth.models import User
from .serializers import UserModelSerializer, UserModelSerializerVersion2


class UserModelViewSet(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


    def get_serializer_class(self):
        if self.request.version == "2.0":
            return UserModelSerializerVersion2
        return UserModelSerializer
