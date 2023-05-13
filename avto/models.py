from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Categoryes(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Car(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField()
    engine_volume = models.FloatField()
    color = models.CharField(max_length=20)
    image = models.ImageField (upload_to='car_images/', null=True, blank=True)
    body_type = models.ForeignKey(Categoryes, on_delete=models.CASCADE)
    mileage = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) {self.body_type}, {self.owner}"
    
