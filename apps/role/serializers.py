from apps.role.models import Role
from rest_framework_json_api import serializers


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Role