from django.http import HttpRequest, HttpResponseRedirect
from CustomAuth.forms import UserLoginForm
from django.contrib.auth import login as user_login
from django.conf import settings
from django.shortcuts import render


def login(request: HttpRequest):
    if not request.user.is_anonymous:
        url = getattr(settings, 'USER_PROFILE_URL', '/profile/')
        return HttpResponseRedirect(url)
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            form.clean()
            user_login(request, form.get_user())
            url = getattr(settings, 'USER_PROFILE_URL', '/profile/')
            return HttpResponseRedirect(url)
        else:
            context = {
                'errors': form.errors,
                'form': UserLoginForm
            }
    else:
        context = {
            'form': UserLoginForm,
        }
    return render(request, 'CustomAuth/pages/login.html', context=context)
