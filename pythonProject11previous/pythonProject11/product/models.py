from django.db import models

class Product(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=30)
    description = models.CharField(max_length=70)
    selling_price = models.IntegerField()
    buying_price = models.IntegerField()

class Storage(models.Model):
    stock_id = models.IntegerField(primary_key=True)
    stock = models.IntegerField()
    stock_buying_price = models.IntegerField()
    stock_selling_price = models.IntegerField()
    purchase = models.IntegerField()


