from django.db import models

class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=40)
    employee_phone = models.CharField(max_length=11)
    employee_email = models.CharField(max_length=30)

class Shipment(models.Model):
    shipment_date = models.TextField()
    tracking_number = models.CharField(max_length=15, primary_key=True)
