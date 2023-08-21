from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from roles.api.serializers import RoleSerializer
from roles.models import Role


class RoleViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
