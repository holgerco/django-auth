import django_tables2 as tables
from CustomAuth.models import User


class UserTable(tables.Table):
    class Meta:
        model = User
        template_name = "django_tables2/bootstrap.html"
        fields = ('email', 'full_name', 'is_verify', 'is_staff', 'is_superuser', 'jalali_last_login',)
