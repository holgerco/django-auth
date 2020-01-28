from CustomAuth.models import User
from CustomAuth.tokens import account_verify_email_token
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.conf import settings


def verify_code(request, verify_uid64, token):
    try:
        uid = force_text(urlsafe_base64_decode(verify_uid64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_verify_email_token.check_token(user, token):
        user.is_verify = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect(getattr(settings, 'VERIFY_SUCCESSFULLY', '/profile/'))
    else:
        return HttpResponse(getattr(settings, 'VERIFY_FAILED', 'Verification link is invalid!'))
