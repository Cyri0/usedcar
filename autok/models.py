from django.db import models

# Create your models here.

class Auto(models.Model):
    brand = models.CharField(max_length=255)
    car_type = models.CharField(max_length=255)
    year = models.IntegerField()
    mileage = models.IntegerField()
    color = models.CharField(max_length=255)

    fuel_options = [
        ('petrol','petrol'),
        ('diesel','diesel'),
        ('lpg','lpg'),
        ('electric','electric')
    ]

    fuel_type = models.CharField(choices=fuel_options, max_length=255)

    def __str__(self):
        return f"{self.brand} - {self.car_type} ({self.year})"