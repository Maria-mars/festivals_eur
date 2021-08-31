from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from apps.promotions.models import Promotions
from apps.promotions.serializers import PromotionSerializer


class PromotionViewSet(ModelViewSet):
    serializer_class = PromotionSerializer
    queryset = Promotions.objects.all()
