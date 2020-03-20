from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import Group, Permission

from django.contrib import auth
from django.core.exceptions import PermissionDenied


def _user_get_permissions(user, obj, from_name):
    permissions = set()
    name = 'get_%s_permissions' % from_name
    for backend in auth.get_backends():
        if hasattr(backend, name):
            permissions.update(getattr(backend, name)(user, obj))
    return permissions


def _user_has_perm(user, perm, obj):
    """
    A backend can raise `PermissionDenied` to short-circuit permission checking.
    """
    for backend in auth.get_backends():
        if not hasattr(backend, 'has_perm'):
            continue
        try:
            if backend.has_perm(user, perm, obj):
                return True
        except PermissionDenied:
            return False
    return False


def _user_has_module_perms(user, app_label):
    """
    A backend can raise `PermissionDenied` to short-circuit permission checking.
    """
    for backend in auth.get_backends():
        if not hasattr(backend, 'has_module_perms'):
            continue
        try:
            if backend.has_module_perms(user, app_label):
                return True
        except PermissionDenied:
            return False
    return False


class PermissionMixin(models.Model):
    is_active = models.BooleanField(
        _('active status'),
        default=True
    )
    is_verify = models.BooleanField(
        _('register status'),
        default=False
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text='Designates whether the user can log into this admin site.'
    )
    is_superuser = models.BooleanField(
        default=False,
        help_text='Designates whether this user should be treated as active.' +
                  'Unselect this instead of deleting accounts.'
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='users',
        related_query_name='user'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="users",
        related_query_name="user",
    )

    class Meta:
        abstract = True

    def get_user_permissions(self, obj=None):
        """
        Return a list of permission strings that this user has directly.
        Query all available auth backends. If an object is passed in,
        return only permissions matching this object.
        """
        return _user_get_permissions(self, obj, 'user')

    def get_group_permissions(self, obj=None):
        """
        Return a list of permission strings that this user has through their
        groups. Query all available auth backends. If an object is passed in,
        return only permissions matching this object.
        """
        return _user_get_permissions(self, obj, 'group')

    def get_all_permissions(self, obj=None):
        return _user_get_permissions(self, obj, 'all')

    def has_perm(self, perm: Permission, obj=None) -> bool:
        if self.is_active and self.is_verify and self.is_superuser:
            return True

        # otherwise we must check the permission
        perm_name = "{}.{}".format(perm.content_type.app_label, perm.codename)
        user_permission: list = list(self.get_user_permissions(obj))
        gp_permission: list = list(self.get_group_permissions(obj))

        for permission in user_permission + gp_permission:
            if perm_name == permission:
                return True

        return False

    def has_module_perms(self, app_label) -> bool:
        if self.is_active and self.is_verify and self.is_superuser:
            return True

        # otherwise we must check the permission
        user_permission: list = list(self.get_user_permissions())
        gp_permission: list = list(self.get_group_permissions())
        for permission in user_permission + gp_permission:
            if app_label == permission.split('.')[0]:
                return True
        return False
