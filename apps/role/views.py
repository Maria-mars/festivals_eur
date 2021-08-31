from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from apps.role.models import Role
from apps.role.serializers import RoleSerializer


class RoleViewSet(ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()