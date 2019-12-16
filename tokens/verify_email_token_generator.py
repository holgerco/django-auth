from django.contrib.auth.tokens import PasswordResetTokenGenerator


class VerifyEmailTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        login_timestamp = '' if user.last_login is None else user.last_login.replace(microsecond=0, tzinfo=None)
        return str(user.pk) + str(timestamp) + str(user.email) + str(user.password) + str(login_timestamp)
