from CustomAuth.models import User
from CustomAuth.tokens import account_verify_email_token
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode


def verify_email(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_verify_email_token.check_token(user, token):
        user.is_register = True
        user.save()
        login(request, user)
        return HttpResponseRedirect('/profile/')
    else:
        return HttpResponse('Activation link is invalid!')
