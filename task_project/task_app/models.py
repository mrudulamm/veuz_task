from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.name)

class CustomField(models.Model):
    label = models.CharField(max_length=255)
    field_type = models.CharField(max_length=20, choices=[
        ('text', 'Text'),
        ('number', 'Number'),
        ('date', 'Date'),
        ('boolean', 'Checkbox'),
    ])

    def __str__(self):
        return '{}'.format(self.label)

class EmployeeCustomField(models.Model):
    employeee = models.ForeignKey(employee, on_delete=models.CASCADE)
    custom_field = models.ForeignKey(CustomField, on_delete=models.CASCADE)
    value = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.employeee.name} - {self.custom_field.label}"