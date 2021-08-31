from rest_framework import routers
from apps.role.views import RoleViewSet

app_name = "role"

router = routers.SimpleRouter()

router.register(r'role', RoleViewSet)
urlpatterns = router.urls
