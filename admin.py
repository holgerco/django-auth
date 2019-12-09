from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, Group
from django.utils.translation import gettext_lazy as _
from .forms.UserForms import UserChangeForm, UserCreationForm
from .models import User


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
                    'permissions'
                ),
            }
        ),
        (
            _('Important dates'), {
                'fields': (
                    'date_register',
                    'last_login',
                    'date_joined',
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

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'is_register')

    search_fields = ('username', 'first_name', 'last_name', 'email', 'groups')

    ordering = ('username',)

    filter_horizontal = ('groups', 'permissions',)


admin.site.register(User)