from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ClientViewSet
from django.urls import path, include

router = SimpleRouter(trailing_slash=False)
router.register("api/client", ClientViewSet, basename="client")


urlpatterns = [
    path("", include(router.urls)),

]
