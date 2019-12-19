from .mixin import MiddlewareMixin
from django.http import HttpRequest, HttpResponse
from CustomAuth.models import User


class JwtMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super(JwtMiddleware, self).__init__()
        self.get_response = get_response

    def process_request(self, request: HttpRequest):
        if not request.user or request.user.is_anonymous:
            jwt_token = request.headers.get('authorization', None)
            print(jwt_token)
            if jwt_token:
                user = User.objects.get_by_token(jwt_token)
                if user:
                    request.user = user

    def process_response(self, request: HttpRequest, response: HttpResponse):
        return response
