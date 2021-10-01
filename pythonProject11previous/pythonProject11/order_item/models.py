from django.db import models

class Order_item(models.Model):
    quantity = models.IntegerField()
    discount = models.IntegerField()
    delivary_charge = models.IntegerField()
    total_price = models.IntegerField()
    transport_cost = models.IntegerField()

class Sales(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    sales=models.IntegerField()




