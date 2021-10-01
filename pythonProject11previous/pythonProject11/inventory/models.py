from django.db import models
from product.models import Product


class Inventory (models.Model):
    inventoy_id = models.IntegerField(primary_key=True)
    barcode = models.IntegerField()
    #product_info = models.ForeignKey(Product, on_delete=models.CASCADE)

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=50)
    #product_info=models.ForeignKey(Product,on_delete=models.CASCADE)


