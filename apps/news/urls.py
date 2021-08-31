from rest_framework import routers
from apps.news.views import NewsViewSet

app_name = "news"

router = routers.SimpleRouter()

router.register(r'newss/', NewsViewSet)
urlpatterns = router.urls

