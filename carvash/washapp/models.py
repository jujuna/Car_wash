from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _




class Washer(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    percentage = models.IntegerField()


    def __str__(self):
        return self.name

class Car(models.Model):
    class CarType(models.TextChoices):
        Sedan="SD",  _("Sedan")
        Hatchback="HT", _("Hatchback")
        Sport="SP", _("Sport")
        Couple="CP", _("Couple")
    number=models.CharField(max_length=7)
    type=models.CharField(
        max_length=2,
        choices=CarType.choices,
        default=CarType.Sedan)
    


    def __str__(self):
        return self.number

class Order(models.Model):
    order_date=models.DateTimeField()
    finish_date=models.DateTimeField()
    price=models.IntegerField()
    washer=models.ForeignKey(Washer, on_delete=models.CASCADE, related_name="washer")
    car=models.ForeignKey(Car,on_delete=models.CASCADE, related_name="car")

    def __str__(self):
        return '{}, {}'.format(self.washer,self.car)
    
    
