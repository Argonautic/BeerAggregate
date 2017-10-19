from django.db import models

class Brewery(models.Model):
    name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    score = models.FloatField(default=0)
    phone = models.CharField(max_length=12, blank=True, default='')
    website = models.CharField(max_length=100, blank=True, default='')
    #may have to add GeoJSON field if address can't do all the lifting

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
