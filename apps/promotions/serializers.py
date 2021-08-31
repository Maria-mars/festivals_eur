from apps.promotions.models import Promotions
from rest_framework_json_api import serializers


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Promotions