from django.contrib.auth.tokens import PasswordResetTokenGenerator


class MagicTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        """
        Make hash value with user attributes and timestamp  
        """
        login_timestamp = '' if user.last_login is None else user.last_login.replace(microsecond=100, tzinfo=None)
        return str(user.pk) + str(user.email) + str(user.password) + str(login_timestamp) + str(timestamp)
