from django.utils.translation import ugettext_lazy as _
from django.db import models
from mezzanine.core.fields import RichTextField


class PointOfInterest(models.Model):
    name = models.CharField(_('name'), max_length=50)
    description = RichTextField(_('Description'), null=True, blank=True)
    lat = models.FloatField(_('Latitude'))
    lng = models.FloatField(_('Longitude'))
    slug = models.SlugField(_('Slug'))

    class Meta:
        verbose_name = _('Point of interest')
        verbose_name_plural = _('Points of interest')

    def __unicode__(self):
        return self.name
