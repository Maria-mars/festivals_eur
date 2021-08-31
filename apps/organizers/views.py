
from rest_framework.viewsets import ModelViewSet
from apps.organizers.models import Organizer
from apps.organizers.serializers import OrganizerSerializer


class OrganizerViewSet(ModelViewSet):
    serializer_class = OrganizerSerializer
    queryset = Organizer.objects.all()
