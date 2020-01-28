from django_tables2 import tables
from CustomAuth.models import PhoneNumberUser


class PhoneUserTable(tables.Table):
    class Meta:
        model = PhoneNumberUser
        template_name = "django_tables2/bootstrap.html"
        fields = ('full_name', 'cellphone', 'email', 'is_verify', 'is_staff', 'is_superuser', 'jalali_last_login',)
