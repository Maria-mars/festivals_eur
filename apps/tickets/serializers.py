from apps.tickets.models import Tickets
from rest_framework_json_api import serializers


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Tickets