from django.db import models
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
VEHICLE_TYPE = (
    ('Two Wheeler', 'Two Wheeler'),
    ('Three Wheeler', 'Three Wheeler'),
    ('Four Wheeler', 'Four Wheeler'),
)

class Vehicle(models.Model):
    vehicle_number      = models.CharField(max_length=50, validators=[alphanumeric])
    vehicle_type        = models.CharField(max_length=50, choices=VEHICLE_TYPE)
    vehicle_model       = models.CharField(max_length=50)
    vehicle_description = models.TextField()

    def __str__(self):
        return self.vehicle_number
    