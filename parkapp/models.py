from pickle import TRUE
from django.db import models

class Region(models.Model):
    region_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'region'
        managed = False

class Park(models.Model):
    id = models.IntegerField(primary_key=True)
    park_name = models.CharField(max_length=100)
    park_latitude = models.FloatField()
    park_longitude = models.FloatField()
    park_address = models.CharField(max_length=100)
    park_tel = models.CharField(max_length=45)
    park_info = models.CharField(max_length=500)
    park_background = models.CharField(max_length=200)
    park_pic = models.CharField(max_length=200)
    park_url = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        db_table = 'park'
        managed = False