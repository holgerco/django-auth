from django.http import HttpRequest, JsonResponse
from CustomAuth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def new_jwt_token(request: HttpRequest):
    """
    If user logged in return user jwt token that expire after 2 month
    :param request: Client request
    :return: A json response that contains jwt-authentication
    """
    user: User = request.user
    token = user.token
    response = {
        'jwt-authentication': token
    }
    return JsonResponse(response, status=200)
