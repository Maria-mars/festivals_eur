from apps.news.models import News
from rest_framework_json_api import serializers


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = News