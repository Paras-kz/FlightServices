from django.db import models

# Create your models here.
class Passengers(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    travelid=models.IntegerField(primary_key=True)
