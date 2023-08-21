from django.urls import path, include
from rest_framework import routers

from missions.api.viewsets import MissionViewSet


missions_router = routers.DefaultRouter()
missions_router.register(
    prefix="missions",
    viewset=MissionViewSet,
    basename="mission",
)

urlpatterns = [
    path("", include(missions_router.urls))
]

