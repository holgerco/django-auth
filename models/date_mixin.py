from django.db import models
from django.utils.translation import gettext_lazy as _


class DateMixin(models.Model):
    date_register = models.DateTimeField(
        _('register date'),
        blank=True,
        null=True
    )

    date_joined = models.DateTimeField(
        _('join date'),
        blank=True,
        null=True,
        auto_now_add=True
    )

    class Meta:
        abstract = True

    pass
