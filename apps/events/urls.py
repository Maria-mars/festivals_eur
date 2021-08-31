from rest_framework import routers
from apps.events.views import EventViewSet

app_name = "events"

router = routers.SimpleRouter()

router.register(r'events/', EventViewSet)
urlpatterns = router.urls

