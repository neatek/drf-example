# from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, mixins
from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
