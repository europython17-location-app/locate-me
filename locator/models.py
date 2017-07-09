from django.db import models
from django.contrib.gis.db import models as gis_model

# Create your models here.

class User(models.Model):
    uuid = models.UUIDField(primary_key=True)

class UserLocation(gis_model.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    coords = gis_model.PointField()
