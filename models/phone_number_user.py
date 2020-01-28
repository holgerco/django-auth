from django.contrib.sites.shortcuts import get_current_site
from .abstract_user import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from kavenegar import *
from django.conf import settings
from CustomAuth.managers import PhoneStaffManager, PhoneUserManager, PhoneSuperuserManager


class PhoneNumberUser(AbstractUser):
    sms_api = KavenegarAPI(getattr(settings, 'KAVENEGAR_API', ''))

    cellphone = PhoneNumberField(
        verbose_name='تلفن همراه',
        region='IR',
        unique=True
    )

    first_name = models.CharField(
        _('نام'),
        max_length=100,
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        _('نام خانوادگی'),
        max_length=200,
        blank=False,
        null=False,
    )

    email = models.EmailField(
        _('ایمیل'),
        max_length=250,
        unique=True,
        blank=True,
        null=True,
        help_text=_('250 characters or fewer.'),
        error_messages={
            'unique': _("A user with that email already exists."),
        }
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'cellphone'
    REQUIRED_FIELDS = []

    objects = PhoneUserManager()
    superusers = PhoneSuperuserManager()
    staff = PhoneStaffManager()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return "%s" % self.full_name

    def send_verification_code(self, request):
        sender = getattr(settings, 'SMS_SENDER')
        receptor = self.cellphone
        link = self.get_magic_link['magic_link']
        current_site = get_current_site(request)
        message = "{}{}".format(current_site.domain, link)
        context = {
            'sender': sender,
            'receptor': receptor,
            'message': message,
        }
        # response = self.sms_api.sms_send(context)
        print(context)
