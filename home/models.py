from django.db import models

# Create your models here.
from django.db import models

class Person(models.Model):
    MARITAL_STATUS_CHOICES = [
        ('married', 'Married'),
        ('unmarried', 'Unmarried'),
    ]
    EMPLOYED_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    college = models.CharField(max_length=200)
    dob = models.DateField()
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)
    employed = models.CharField(max_length=3, choices=EMPLOYED_CHOICES)

    def __str__(self):
        return self.name