from django.contrib.auth.backends import BaseBackend
from CustomAuth.models import User
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
from CustomAuth.tokens import magic_token


class MagicLinkBackend(BaseBackend):
    def get_user(self, uidb64):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        return user

    def authenticate(self, request, uidb64, token):
        user = self.get_user(uidb64)
        if user is not None and magic_token.check_token(user, token):
            return user
        else:
            return None
