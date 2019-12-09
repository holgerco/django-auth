from django.db import models
from django.utils.translation import gettext_lazy as _


class FinanceMixin(models.Model):
    wallet = models.PositiveIntegerField(
        _('Credit of user'),
        default=0
    )
