from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _



class Location(models.Model):
        address = models.CharField(max_length=100)
        city = models.CharField(max_length=100)

        def __str__(self):
            return self.address

class WasherCompany(models.Model):
    name=models.CharField(max_length=100)
    number_of_cabins=models.PositiveSmallIntegerField()
    locations=models.ManyToManyField(Location,  related_name="location")

    def __str__(self):
        return self.name

class HireCompany(models.Model):
    class CarType(models.TextChoices):
        Sedan="SD",  _("Sedan")
        Hatchback="HT", _("Hatchback")
        Sport="SP", _("Sport")
        Couple="CP", _("Couple")
    
    
    company=models.ForeignKey(WasherCompany, on_delete=models.CASCADE, related_name="company")
    cartype=models.CharField(
        max_length=2,
        choices=CarType.choices,
        default=CarType.Sedan,
    )
    date=models.DateTimeField(auto_now_add=True,)
    date.editable=True
   

    def __str__(self):
        return 'company -> {}, type -> {}'.format(self.company,self.get_cartype_display())