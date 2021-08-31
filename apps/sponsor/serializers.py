from apps.sponsor.models import Sponsor
from rest_framework_json_api import serializers


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Sponsor
