from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms.UserForms import UserChangeForm, UserCreationForm
from .models import User
from django.contrib.auth.models import Group, Permission


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    fieldsets = (
        (
            None, {
                'fields': (
                    'username',
                    'password'
                )
            }
        ),
        (
            _('Personal info'), {
                'fields': (
                    'first_name',
                    'last_name',
                    'email'
                )
            }
        ),
        (
            _('finance'), {
                'fields': (
                    'wallet',
                )
            }
        ),
        (
            _('Permissions'), {
                'fields': (
                    'is_active',
                    'is_register',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions'
                ),
            }
        ),
        (
            _('Important dates'), {
                'fields': (
                    'date_verify',
                    'last_login',
                )
            }
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_verify')

    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'is_verify')

    search_fields = ('username', 'first_name', 'last_name', 'email', 'groups')

    ordering = ('username',)

    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)
admin.site.register(Permission)
