from rest_framework import mixins, viewsets

from api.mixins import StaffEditorPermissionMixin
from api.permissions import BasicPermissions
from core.models import Technology

from .serializers import TechnologySerializer
from rest_framework import permissions
class CustomGenericViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.IsAdminUser]
    # def get_permissions(self):
    #     """
    #     Instantiates and returns the list of permissions that this view requires.
    #     """
    #     # if self.action == 'list':
    #     #     permission_classes = []
    #     # else:
    #     #     permission_classes = []
    #     print()
    #     return [permission() for permission in self.permission_classes]

class ReadonlyGenericViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        StaffEditorPermissionMixin,
        CustomGenericViewSet):
    """
    get -> list -> Queryset
    get -> retrieve -> Model Instance Detail View
    """
    lookup_field = 'pk'
    permission_classes = [BasicPermissions]

class TechnologyGenericViewSet(ReadonlyGenericViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [permissions.AllowAny]