
from django.db import models


if '_' not in locals():
    def _(s): return s


class Hotel(models.Model):
    """
    Hotel
    """

    name = models.CharField(verbose_name=_(
        'Name'), null=True, blank=True, max_length=100, default='')
    description = models.CharField(verbose_name=_(
        'Description'), null=True, blank=True, max_length=100, default='')

    class Meta:
        verbose_name = _("Hotel")
