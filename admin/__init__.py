from django.contrib import admin
from django.contrib.auth.models import Permission
from .user_admin import UserAdmin
from .phone_user_admin import PhoneUserAdmin
from CustomAuth.models import User, PhoneNumberUser
from django.conf import settings

admin.site.register(Permission)

if hasattr(settings, 'AUTH_USER_MODEL') and settings.AUTH_USER_MODEL == 'CustomAuth.PhoneNumberUser':
    admin.site.register(PhoneNumberUser, PhoneUserAdmin)
else:
    admin.site.register(User, UserAdmin)
