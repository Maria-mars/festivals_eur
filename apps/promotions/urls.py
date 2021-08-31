from rest_framework import routers
from apps.promotions.views import PromotionViewSet

app_name = "promotions"

router = routers.SimpleRouter()

router.register(r'promotion', PromotionViewSet)
urlpatterns = router.urls
