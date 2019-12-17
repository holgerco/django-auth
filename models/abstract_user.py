from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from .permission_mixin import PermissionMixin
from .date_mixin import DateMixin
from django.core.mail import send_mail
from django.utils import timezone
from ..managers import UserManager
from .finance_mixin import FinanceMixin
from .profile import Profile
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from CustomAuth.tokens import account_verify_email_token, magic_token
from smtplib import SMTPException


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

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    @property
    def full_name(self):
        return self.get_full_name()

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

    def verification_email(self, request):
        current_site = get_current_site(request)
        mail_subject = getattr(settings, 'REGISTRATION_MAIL_SUBJECT', 'Activate your blog account.')
        context = {
            'user': self,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(self.pk)),
            'token': account_verify_email_token.make_token(self)
        }
        message = render_to_string('CustomAuth/pages/email_verification.html', context=context)
        try:
            self.email_user(mail_subject, message, from_email=settings.EMAIL_FROM)
        except (SMTPException, Exception):
            print(message)

    def get_magic_link(self, request):
        current_site = get_current_site(request)
        uidb64 = urlsafe_base64_encode((force_bytes(self.pk)))
        token = magic_token.make_token(self)
        magic_link = 'http://{}/{}/{}'.format(current_site.domain, uidb64, token)
        print(magic_link)
        return magic_link
