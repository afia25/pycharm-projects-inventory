from django.db import models

class Customer(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    delivary_address = models.CharField(max_length=150)

class Payment(models.Model):
    payment_method = models.TextField()
    payment_status = models.TextField()
    #due_payment = models.IntegerField()
