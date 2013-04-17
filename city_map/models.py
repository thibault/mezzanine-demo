from django.utils.translation import ugettext_lazy as _
from django.db import models


class PointOfInterest(models.Model):
    lat = models.FloatField(_('Latitude'))
    lng = models.FloatField(_('Longitude'))
    name = models.CharField(_('name'), max_length=50)
    description = models.TextField(_('Description'), null=True, blank=True)

    class Meta:
        verbose_name = _('Point of interest')
        verbose_name_plural = _('Points of interest')

    def __unicode__(self):
        return self.name
