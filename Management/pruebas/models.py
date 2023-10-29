from django.db import models

# Create your models here.



class Treatment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    treatments = models.ManyToManyField(Treatment)

class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    doctor = models.CharField(max_length=100)
    
    # You can add more fields as needed for your application

    def __str__(self):
        return f"Appointment on {self.date} at {self.time} with Dr. {self.doctor}"
