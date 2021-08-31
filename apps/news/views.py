from rest_framework.viewsets import ModelViewSet
from apps.news.models import News
from apps.news.serializers import NewsSerializer


class NewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()