from django.db import models
from django.utils.translation import gettext_lazy as _
from jdatetime import datetime as jalali


class DateMixin(models.Model):
    date_verify = models.DateTimeField(
        _('verify date'),
        blank=True,
        null=True
    )

    date_joined = models.DateTimeField(
        _('join date'),
        blank=True,
        null=True,
        auto_now_add=True
    )

    @property
    def jalali_date_verify(self):
        return jalali.fromgregorian(datetime=self.date_verify).strftime("%d %b %Y")

    def jalali_date_joined(self):
        return jalali.fromgregorian(datetime=self.date_joined).strftime("%d %b %Y")

    class Meta:
        abstract = True

    pass
