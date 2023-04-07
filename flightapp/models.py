from django.db import models

# Create your models here.
class Flight(models.Model):
    flightNumber=models.CharField(max_length=10)
    operatingAirlines=models.CharField(max_length=20)
    departureCity=models.CharField(max_length=20)
    arrivalCity=models.CharField(max_length=20)
    dateOfDeparture=models.DateField()
    estimatedTimeOfDeparture=models.TimeField()
class Passenger(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    middleName=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    phone=models.CharField(max_length=12)

class Reservation(models.Model):
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
    # using keyword foreign key relation becomes OnetoMany
    #one flight can have many reservation
    passenger=models.OneToOneField(Passenger,on_delete=models.CASCADE)
    
