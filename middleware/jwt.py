from .mixin import MiddlewareMixin
from django.http import HttpRequest, HttpResponse
from CustomAuth.models import User
from django.contrib.auth import get_user_model


class JwtMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super(JwtMiddleware, self).__init__()
        self.get_response = get_response

    def process_request(self, request: HttpRequest):
        """
        If the request contains a header 'jwt-authentication'.
        Tries token sent by the user to identify the applicant.\n
        :param request: A request that the middleware is checked
        :return:
        """
        if not request.user or request.user.is_anonymous:
            jwt_token = request.headers.get('jwt-authentication', None)
            if jwt_token:
                user = get_user_model().objects.get_by_token(jwt_token)
                if user:
                    request.user = user

    def process_response(self, request: HttpRequest, response: HttpResponse):
        return response
