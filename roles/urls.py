from django.urls import path, include
from rest_framework import routers

from roles  .api.viewsets import RoleViewSet


roles_router = routers.DefaultRouter()
roles_router.register(
    prefix="",
    viewset=RoleViewSet,
    basename="roles",
)

urlpatterns = [
    path("", include(roles_router.urls))
]

