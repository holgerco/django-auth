from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from .permission_mixin import PermissionMixin
from .date_mixin import DateMixin
from django.core.mail import send_mail
from django.utils import timezone
from CustomAuth.managers import UserManager, SuperuserManager, StaffManager
from .finance_mixin import FinanceMixin
from .profile import Profile
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from CustomAuth.tokens import account_verify_email_token, magic_token
from smtplib import SMTPException
import jwt
from jdatetime import datetime as jalali
from django_cryptography.core import signing


class AbstractUser(AbstractBaseUser, PermissionMixin, DateMixin, FinanceMixin):
    username_validator = UnicodeUsernameValidator()

    first_name = models.CharField(
        _('first name'),
        max_length=100,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=200,
        blank=True,
        null=True,
    )

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        blank=True,
        null=True,
        help_text=_('150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        }
    )

    email = models.EmailField(
        _('email address'),
        max_length=250,
        unique=True,
        help_text=_('Required, 250 characters or fewer.'),
        error_messages={
            'unique': _("A user with that email already exists."),
        }
    )

    objects = UserManager()
    superusers = SuperuserManager()
    staff = StaffManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    @property
    def full_name(self):
        return self.get_full_name()

    @property
    def jalali_last_login(self):
        return jalali.fromgregorian(datetime=self.last_login).strftime("%d %m %Y")

    def __str__(self):
        if self.username is None:
            return "%s" % self.email
        return "@%s : %s" % (self.username, self.email)

    def register_user(self):
        self.data_register = timezone.now()
        self.is_verify = True
        self.save(update_fields=['date_register', 'is_register'])

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        if (not self.first_name) or (not self.last_name):
            full_name = '---'
        else:
            full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def profile(self):
        if not hasattr(self, '_profile') or not self._profile:
            self._profile = None
            for field in self._meta.get_fields():
                field_name = field.name
                value = getattr(self, field_name, None)
                if value and isinstance(value, Profile):
                    self._profile = value
        return self._profile

    def send_verification_code(self, request):
        current_site = get_current_site(request)
        mail_subject = getattr(settings, 'REGISTRATION_MAIL_SUBJECT', 'Activate your blog account.')
        context = {
            'user': self,
            'domain': current_site.domain,
            'verify_uid64': urlsafe_base64_encode(force_bytes(self.pk)),
            'token': account_verify_email_token.make_token(self)
        }
        message = render_to_string('CustomAuth/pages/email_verification.html', context=context)
        try:
            self.email_user(mail_subject, message, from_email=settings.EMAIL_FROM)
        except (SMTPException, Exception):
            print(message)

    @property
    def get_magic_link(self):
        """
        Return a magic url that with that can login automatic
        :return: Return a dictionary that contains uid64, token and magic_link
        """
        uid64 = urlsafe_base64_encode((force_bytes(self.pk)))
        token = magic_token.make_token(self)
        magic_link = '{}/{}'.format(uid64, token)
        return {
            'uid64': uid64,
            'token': token,
            'magic_link': magic_link
        }

    @property
    def token(self):
        """
        :return: Return jwt token
        """
        return self.generate_jwt_token()

    def generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 30 days into the future.
        """
        dt = timezone.datetime.now() + timezone.timedelta(days=30)

        token = jwt.encode(
            payload={
                'id': self.pk,
                'exp': dt
            },
            key=settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    def digital_sign(self, days: int = None):
        if days:
            dt = timezone.datetime.now() + timezone.timedelta(days=days)
            timed_sign = jwt.encode(
                payload={
                    'sign': signing.dumps(self.id),
                    'exp': dt
                },
                key=settings.SECRET_KEY,
                algorithm='HS256'
            )

            return timed_sign.decode('utf-8')
        else:
            sign = jwt.encode(
                payload={
                    'sign': signing.dumps(self.id),
                },
                key=settings.SECRET_KEY,
                algorithm='HS256'
            )

            return sign.decode('utf-8')
