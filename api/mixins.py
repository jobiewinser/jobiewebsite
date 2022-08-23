from .permissions import BasicPermissions
from rest_framework import permissions
from django.db.models import Q
class StaffEditorPermissionMixin():
    permission_classes = [BasicPermissions, permissions.IsAdminUser]
    
class UserQuerySetMixin():
    user_fields = ['user']
    allow_staff_view = False
    def get_queryset(self, *args, **kwargs):
        args = Q()  #defining args as empty Q class object to handle empty args_list
        for each_args in self.user_fields:
            args |= Q(**{each_args:self.request.user} )

        qs = super().get_queryset().filter(*(args,) )
        return qs