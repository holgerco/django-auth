from django.http import HttpRequest, JsonResponse
from CustomAuth.models import User
from CustomAuth.decorators import jwt_required


@jwt_required
def new_jwt_token(request: HttpRequest):
    user: User = request.user
    token = user.token
    response = {
        'jwt-authentication': token
    }
    return JsonResponse(response, status=200)
