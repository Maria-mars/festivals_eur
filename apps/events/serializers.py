from apps.events.models import Events
from rest_framework_json_api import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Events