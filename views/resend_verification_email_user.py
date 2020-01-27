from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from CustomAuth.models import User


@login_required(login_url='/login/')
def resend_verification_code(request: HttpRequest):
    user: User = request.user
    context = {}
    if not user.is_verify:
        user.verification_email(request)
    else:
        context = {
            'user_already_verified': True
        }
    return render(request, 'CustomAuth/pages/resend_verification_code.html', context=context)
