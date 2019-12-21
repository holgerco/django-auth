from django.http import HttpRequest, JsonResponse
from CustomAuth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def revoke(request: HttpRequest):
    user: User = request.user
    token = user.token
    response = {
        'jwt-authentication': token
    }
    return JsonResponse(response, status=200)
