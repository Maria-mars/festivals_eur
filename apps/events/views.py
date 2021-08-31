
from rest_framework.viewsets import ModelViewSet
from apps.events.models import Events
from apps.events.serializers import EventSerializer


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Events.objects.all()