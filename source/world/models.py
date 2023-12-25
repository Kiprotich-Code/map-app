from django.db import models
from django.contrib.gis.db import models as geomodels

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100, blank=False)
    geometry = geomodels.PointField()

    class Meta:
        ordering = ('name', )

        verbose_name_plural = 'cities'