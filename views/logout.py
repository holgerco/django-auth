from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth import logout as user_logout
from django.conf import settings


def logout(request: HttpRequest):
    user_logout(request)
    return HttpResponseRedirect(getattr(settings, 'LOGOUT_REDIRECT', '/'))
