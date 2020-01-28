from .date_mixin import DateMixin
from .permission_mixin import PermissionMixin
from .abstract_user import AbstractUser
from .user import User
from .profile import Profile
from .phone_number_user import PhoneNumberUser
from django.utils import timezone


def update_last_login(sender, auth_user, **kwargs):
    """
    A signal receiver which updates the last_login date for
    the user logging in.
    """
    auth_user.last_login = timezone.now()
    auth_user.save(update_fields=['last_login'])
