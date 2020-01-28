from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.conf import settings


class VerifyEmailTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        login_timestamp = '' if user.last_login is None else user.last_login.replace(microsecond=0, tzinfo=None)
        if hasattr(settings, 'AUTH_USER_MODEL') and \
                getattr(settings, 'AUTH_USER_MODEL') == 'CustomAuth.PhoneNumberUser':
            return str(user.pk) + str(timestamp) + str(user.cellphone) + str(user.password) + str(login_timestamp)
        return str(user.pk) + str(timestamp) + str(user.email) + str(user.password) + str(login_timestamp)
