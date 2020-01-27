from django.http import HttpRequest, JsonResponse
from CustomAuth.models import User


def jwt(function):
    """
    :param function: The view function that call with a url that client request
    :return: if user has jwt authentication and is not anonymous call function,
        else response 403
    """

    def wrap(request: HttpRequest, *args, **kwargs):
        user: User = request.user
        is_jwt_authentication = request.headers.__contains__('jwt-authentication')
        if not user.is_anonymous and is_jwt_authentication:
            return function(request, *args, *kwargs)
        else:
            context = {
                'error': 'jwt authentication is required'
            }
            return JsonResponse(context, status=403)

    return wrap
