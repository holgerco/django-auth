from django.http import HttpRequest
from django.shortcuts import render
from django_tables2 import SingleTableView
from django_tables2.paginators import LazyPaginator
from django_tables2.config import RequestConfig
from CustomAuth.tables import UserTable
from CustomAuth.models import User
from CustomAuth.decorators import superuser_only


@superuser_only
def user_list(request: HttpRequest):
    table = UserTable(User.objects.all())
    RequestConfig(request=request, paginate={"paginator_class": LazyPaginator}).configure(table)
    context = {
        'table': table
    }
    return render(request, 'CustomAuth/pages/tables.html', context=context)


@superuser_only
def superuser_list(request: HttpRequest):
    table = UserTable(User.superusers.all())
    RequestConfig(request=request, paginate={"paginator_class": LazyPaginator}).configure(table)
    context = {
        'table': table
    }
    return render(request, 'CustomAuth/pages/tables.html', context=context)


@superuser_only
def staff_list(request: HttpRequest):
    table = UserTable(User.staff.all())
    RequestConfig(request=request, paginate={"paginator_class": LazyPaginator}).configure(table)
    context = {
        'table': table
    }
    return render(request, 'CustomAuth/pages/tables.html', context=context)
