from django.urls import path, include
from rest_framework import routers

from missions.api.viewsets import MissionViewSet


missions_router = routers.DefaultRouter()
missions_router.register(
    prefix="",
    viewset=MissionViewSet,
    basename="mission",
)

urlpatterns = [
    path("missions", include(missions_router.urls))
]

