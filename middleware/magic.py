from CustomAuth.backends import MagicLinkBackend
from CustomAuth.middleware import MiddlewareMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.conf import settings


class MagicMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super(MagicMiddleware, self).__init__()
        self.get_response = get_response
        self.magic_link_backend = MagicLinkBackend()

    def process_request(self, request: HttpRequest):
        pass

    def process_response(self, request: HttpRequest, response: HttpResponse):
        return response

    def process_view(self, request: HttpRequest, view_func, view_args: list, view_kwargs: dict):
        uid64 = view_kwargs.get('magic_uid64', None)  # get user id base on uid64
        token = view_kwargs.get('token', None)  # get
        if uid64 and token:
            backend = MagicLinkBackend()
            user = backend.authenticate(request, uid64, token)
            if user:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                profile_url = getattr(settings, 'USER_PROFILE_URL', '/profile/')
                return HttpResponseRedirect(profile_url)
        return None
