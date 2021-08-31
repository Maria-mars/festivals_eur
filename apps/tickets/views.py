from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from apps.tickets.models import Tickets
from apps.tickets.serializers import TicketSerializer


class TicketsViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Tickets.objects.all()