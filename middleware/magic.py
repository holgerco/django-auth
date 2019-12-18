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
        uidb64 = view_kwargs.get('uidb64', None)
        token = view_kwargs.get('token', None)
        if uidb64 and token:
            backend = MagicLinkBackend()
            user = backend.authenticate(request, uidb64, token)
            if user:
                login(request, user)
                profile_url = getattr(settings, 'USER_PROFILE_URL', '/profile/')
                return HttpResponseRedirect(profile_url)
        return None
