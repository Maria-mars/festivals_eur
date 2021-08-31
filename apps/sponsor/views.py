from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from apps.sponsor.models import Sponsor
from apps.sponsor.serializers import SponsorSerializer


class SponsorsViewSet(ModelViewSet):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()