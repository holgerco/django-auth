from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from CustomAuth.forms import PhoneUserCreationForm, PhoneUserChangeForm
from phonenumber_field import widgets, modelfields


class PhoneUserAdmin(BaseUserAdmin):
    form = PhoneUserChangeForm
    add_form = PhoneUserCreationForm
    formfield_overrides = {
        modelfields.PhoneNumberField: {
            'widget': widgets.PhoneNumberPrefixWidget
        }
    }
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
                    'cellphone',
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
                    'is_verify',
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
            'fields': ('cellphone', 'password1', 'password2'),
        }),
    )

    list_display = ('cellphone', 'first_name', 'last_name', 'email', 'is_verify')

    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'is_verify')

    search_fields = ('username', 'first_name', 'last_name', 'email', 'groups', 'cellphone')

    ordering = ('username',)

    filter_horizontal = ('groups', 'user_permissions',)
