from django.db import models
from django.contrib.gis.db import models as gis_model

# Create your models here.

class User(models.Model):
    uuid = models.UUIDField(primary_key=True)

class UserLocation(gis_model.Model):
    user = models.ForeignObject(to=User, on_delete=None, from_fields=[])
    coords = gis_model.PointField()
