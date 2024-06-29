from django.db import models

class Street(models.Model):
    stt = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    importance_level = models.CharField(max_length=200, blank=True, null=True)
    significance = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name
