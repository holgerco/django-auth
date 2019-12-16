from django.http import HttpRequest, HttpResponseRedirect
from CustomAuth.forms import UserCreationForm
from django.contrib.auth import login
from django.conf import settings
from django.shortcuts import render


def signup(request: HttpRequest):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid() and form.clean_password2():
            user = form.save()
            user.save()
            login(request, user)
            user.verification_email(request)
            return HttpResponseRedirect(getattr(settings, 'SIGNUP_SUCCESSFULLY_URL', '/profile/'))
        else:
            context = {
                'errors': form.errors,
                'form': UserCreationForm,
            }
    else:
        context = {
            'form': UserCreationForm
        }
    return render(request, 'CustomAuth/pages/signup.html', context)
