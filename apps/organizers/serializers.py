from apps.organizers.models import Organizer
from rest_framework_json_api import serializers


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Organizer
