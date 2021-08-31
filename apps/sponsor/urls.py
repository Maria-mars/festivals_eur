from rest_framework import routers
from apps.sponsor.views import SponsorsViewSet

app_name = "sponsor"
router = routers.SimpleRouter()


router.register(r'Sponsor', SponsorsViewSet)
urlpatterns = router.urls
