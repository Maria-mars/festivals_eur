from rest_framework import routers
from apps.tickets.views import TicketsViewSet

app_name = "tickets"
router = routers.SimpleRouter()

router.register(r'views', TicketsViewSet)
urlpatterns = router.urls
