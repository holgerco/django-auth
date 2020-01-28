from django.http import HttpRequest
from django.shortcuts import render
from django.conf import settings
from django_tables2.paginators import LazyPaginator
from django_tables2.config import RequestConfig
from CustomAuth.tables import UserTable, PhoneUserTable
from CustomAuth.models import User, PhoneNumberUser
from CustomAuth.decorators import superuser_only


@superuser_only
def user_list(request: HttpRequest):
    if hasattr(settings, 'AUTH_USER_MODEL') and settings.AUTH_USER_MODEL == 'CustomAuth.PhoneNumberUser':
        table = PhoneUserTable(PhoneNumberUser.objects.all())
    else:
        table = UserTable(User.objects.all())
    RequestConfig(request=request, paginate={"paginator_class": LazyPaginator}).configure(table)
    context = {
        'table': table
    }
    return render(request, 'CustomAuth/pages/tables.html', context=context)


@superuser_only
def superuser_list(request: HttpRequest):
    if hasattr(settings, 'AUTH_USER_MODEL') and settings.AUTH_USER_MODEL == 'CustomAuth.PhoneNumberUser':
        table = PhoneUserTable(PhoneNumberUser.superusers.all())
    else:
        table = UserTable(User.superusers.all())
    RequestConfig(request=request, paginate={"paginator_class": LazyPaginator}).configure(table)
    context = {
        'table': table
    }
    return render(request, 'CustomAuth/pages/tables.html', context=context)


@superuser_only
def staff_list(request: HttpRequest):
    if hasattr(settings, 'AUTH_USER_MODEL') and settings.AUTH_USER_MODEL == 'CustomAuth.PhoneNumberUser':
        table = PhoneUserTable(PhoneNumberUser.staff.all())
    else:
        table = UserTable(User.staff.all())
    RequestConfig(request=request, paginate={"paginator_class": LazyPaginator}).configure(table)
    context = {
        'table': table
    }
    return render(request, 'CustomAuth/pages/tables.html', context=context)
